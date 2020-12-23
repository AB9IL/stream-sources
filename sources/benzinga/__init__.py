from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'benzinga',
        'url': 'https://www.benzinga.com',
    }

    FEED_URL = 'https://www.benzinga.com/feeds/list'
