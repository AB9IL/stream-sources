from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'benzinga',
        'category': 'initiation',
        'url': 'https://www.benzinga.com/',
    }

    FEED_URL = 'https://www.benzinga.com/analyst-ratings/initiation/feed'
