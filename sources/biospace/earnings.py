from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'biospace',
        'category': 'earnings',
        'url': 'https://www.biospace.com/',
    }

    FEED_URL = 'https://feedity.com/biospace-com/WlpaV1VX.rss'
