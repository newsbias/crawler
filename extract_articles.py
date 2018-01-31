import os
import sys
import newsapi
import multiprocessing
import requests
import readability
import lxml.html


def extract_article_text(article):
    resp = requests.get(article['url'])
    doc = readability.Document(resp.text)

    summary = doc.summary()
    body = lxml.html.document_fromstring(summary)

    return {
        'title': doc.title(),
        'clean_html': summary,
        'body_text': body.text_content()
    }


def print_article_output(postproc_article):
    print('--- {} ---'.format(postproc_article['title']))
    print(postproc_article['body_text'])
    print()


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

    with multiprocessing.Pool() as p:
        for postproc_article in p.imap_unordered(
                extract_article_text, articles):
            print_article_output(postproc_article)


if __name__ == '__main__':
    main()
