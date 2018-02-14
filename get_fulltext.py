import sys
import requests
import readability
import lxml.html


def extract_fulltext(url):
    resp = requests.get(url)
    doc = readability.Document(resp.text)

    summary = doc.summary()
    body = lxml.html.document_fromstring(summary)

    return body.text_content()


def main():
    if len(sys.argv) < 2:
        print('usage: {} [url]'.format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    print(extract_fulltext(sys.argv[1]))


if __name__ == '__main__':
    main()
