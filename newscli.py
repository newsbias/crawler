import os
import sys
import newsapi


def main():
    apikey = os.environ.get('NB_NEWSAPI_API_KEY', None)
    if apikey is None:
        print('API key not specified', file=sys.stderr)
        sys.exit(1)
    client = newsapi.Client(apikey)

    if len(sys.argv) <= 1:
        print('usage: {} [query]'.format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)
    query = ' '.join(sys.argv[1:])
    articles = client.query(query)

    for a in articles:
        print('--- {} ---'.format(a['title']))
        print(a['description'])
        print()


if __name__ == '__main__':
    main()
