import os


import fix_path


import tweepy
from flask import Flask
from dotenv import load_dotenv

from utils.gcp_secrets import GCPSecretHandler
from utils.gcp_writer import GCPWriter
from utils.twitter_streamer import StreamListenerImpl

from google.cloud import storage
from google.cloud import secretmanager

storage_client = storage.Client()
secret_client = secretmanager.SecretManagerServiceClient()

load_dotenv()
auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)


gcp_secret_handler = GCPSecretHandler(secret_client)

gcp_writer = GCPWriter(storage_client)

streamListener = StreamListenerImpl(gcp_writer)

myStream = tweepy.Stream(auth=api.auth, listener=streamListener)


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"


@app.route('/track/<topic>')
def track_topic(topic):
    streamListener.start()
    myStream.filter(track=[topic], is_async=True)
    return 'Getting Your Topic'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
