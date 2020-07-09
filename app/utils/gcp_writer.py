import pandas as pd


class GCPWriter:

    def __init__(self, storage_client):
        self._df = pd.DataFrame(columns=["user_id", "user_name", "tweet_id", "tweet_text"])
        self._bucket = storage_client.get_bucket('sentimentef9cfe64')
        self._client = storage_client

    def add_record(self, row):
        self._df = self._df.append(row, ignore_index=True)
        if len(self._df) == 10:
            self._bucket.blob('upload_test/test.csv').upload_from_string(self._df.to_csv(), 'text/csv')
