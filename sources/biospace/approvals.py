from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'biospace',
        'category': 'approvals',
        'url': 'https://www.biospace.com/',
    }

    FEED_URL = 'https://feedity.com/biospace-com/WlpaV1tX.rss'
