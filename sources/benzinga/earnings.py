from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'benzinga',
        'category': 'earnings',
        'url': 'https://www.benzinga.com/',
    }

    FEED_URL = 'https://www.benzinga.com/news/earnings/feed'
