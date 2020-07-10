import os

import fix_path

import tweepy
from flask import Flask

from utils.gcp_secrets import GCPSecretHandler
from utils.gcp_writer import GCPWriter
from utils.twitter_streamer import StreamListenerImpl

from google.cloud import storage
from google.cloud import secretmanager

project_id = os.getenv('GOOGLE_CLOUD_PROJECT')

storage_client = storage.Client()
secret_client = secretmanager.SecretManagerServiceClient()

gcp_secret_handler = GCPSecretHandler(project_id, secret_client)
gcp_writer = GCPWriter(project_id, storage_client)
streamListener = StreamListenerImpl(gcp_writer)

auth = tweepy.OAuthHandler(gcp_secret_handler.get_tck(), gcp_secret_handler.get_tcs())
auth.set_access_token(gcp_secret_handler.get_tat(), gcp_secret_handler.get_tats())
api = tweepy.API(auth)
myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"


@app.route('/track/<topic>')
def track_topic(topic):
    myStream.filter(track=[topic], is_async=True)
    return 'Getting Your Topic'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
