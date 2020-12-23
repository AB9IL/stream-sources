from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'biospace',
        'category': 'products',
        'url': 'https://www.biospace.com/',
    }

    FEED_URL = 'https://feedity.com/biospace-com/WlpaV1VQ.rss'
