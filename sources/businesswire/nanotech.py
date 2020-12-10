from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'businesswire',
        'category': 'nanotech',
        'url': 'https://www.businesswire.com/',
    }

    FEED_URL = 'https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeGVtRWQ=='
