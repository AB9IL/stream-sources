from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'benzinga',
        'category': 'small-cap-analysis',
        'url': 'https://www.benzinga.com/',
    }

    FEED_URL = 'https://www.benzinga.com/trading-ideas/small-cap-analysis/feed'
