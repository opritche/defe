import feedparser

url = "https://techcrunch.com/feed/"
feed = feedparser.parse(url)


def techcrunch():
    return feed.entries
