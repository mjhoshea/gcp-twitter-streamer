class GCPSecretHandler:

    def __init__(self, project, secret_client):
        self._client = secret_client
        self._project = project
        self._twitter_consumer_key = self.access_secret_version("twitter_consumer_key", "latest")
        self._twitter_consumer_secret = self.access_secret_version("twitter_consumer_secret", "latest")
        self._twitter_access_token = self.access_secret_version("twitter_access_token", "latest")
        self._twitter_access_token_secret = self.access_secret_version("twitter_access_token_secret", "latest")

    def get_tck(self):
        return self._twitter_consumer_key

    def get_tcs(self):
        return self._twitter_consumer_secret

    def get_tat(self):
        return self._twitter_access_token

    def get_tats(self):
        return self._twitter_access_token_secret

    def access_secret_version(self, secret_id, version_id):
        """
        Access the payload for the given secret version if one exists. The version
        can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
        """

        # Build the resource name of the secret version.
        name = self._client.secret_version_path(self._project, secret_id, version_id)

        # Access the secret version.
        response = self._client.access_secret_version(name)

        payload = response.payload.data.decode('UTF-8')
        return payload
