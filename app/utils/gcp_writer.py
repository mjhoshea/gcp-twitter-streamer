import pandas as pd
import time


class GCPWriter:

    def __init__(self, project, storage_client):
        self._df = pd.DataFrame(columns=["user_id", "user_name", "tweet_id", "tweet_text"])
        self._bucket = storage_client.get_bucket(project)
        self._client = storage_client

    def add_record(self, row):
        self._df = self._df.append(row, ignore_index=True)
        if len(self._df) == 10:
            time_stamp = int(time.time())
            self._bucket.blob(f'batch_{time_stamp}/tweets.csv').upload_from_string(self._df.to_csv(), 'text/csv')
