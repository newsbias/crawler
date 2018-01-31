import requests

URL = 'https://newsapi.org/v2/everything'


class NewsApiError(Exception):
    pass


class Client:
    def __init__(self, api_key):
        self.api_key = api_key

    def query(self, q):
        query_pairs = {
            'apikey': self.api_key,
            'language': 'en',
            'sortBy': 'publishedAt',
            'q': q
        }
        resp = requests.get(URL, params=query_pairs)
        resp.raise_for_status()
        data = resp.json()
        if data['status'] != 'ok':
            raise NewsApiError
        return data['articles']
