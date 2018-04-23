
#!/usr/bin/env python3

import urllib.request
from lxml import etree, objectify


def _download_webpage(url):
    return urllib.request.urlopen(url)


def _get_xpath_content(html, xpath):
    parser = etree.HTMLParser()
    tree = etree.parse(html, parser)
    content = tree.xpath(xpath)
    return content[0]


def get_content(url, xpath):
    html = _download_webpage(url)
    content = _get_xpath_content(html, xpath)
    return content


if __name__ == "__main__":
    url = 'http://www.google.com'
    content = get_content(url, "//div[@id='guser']")
    print(repr(content))
    print(objectify.dump(content))