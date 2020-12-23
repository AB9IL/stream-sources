from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'benzinga',
        'category': 'biotech',
        'url': 'https://www.benzinga.com/',
    }

    FEED_URL = 'https://www.benzinga.com/general/biotech/feed'
