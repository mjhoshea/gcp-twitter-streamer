from tweepy import StreamListener
import json


class StreamListenerImpl(StreamListener):

    def __init__(self, gcp_writer):
        super().__init__()
        self._gcp_writer = gcp_writer

    def on_data(self, raw_data):
        tweet_dict = json.loads(raw_data)
        if 'retweeted_status' not in tweet_dict.keys():
            user_id = tweet_dict['user']['id_str']
            user_name = tweet_dict['user']['screen_name']
            tweet_id = tweet_dict['id']
            tweet_text = tweet_dict['extended_tweet']['full_text']
            row_dict = dict(zip((
                "user_id", "user_name", "tweet_id", "tweet_text"),
                (user_id,  user_name, tweet_id, tweet_text))
            )
            self._gcp_writer.add_record(row_dict)

    def on_status(self, status):
        print(status.text)

    def stop(self):
        self.contin = False

    def start(self):
        self.contin = True

