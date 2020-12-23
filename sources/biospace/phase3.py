from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'biospace',
        'category': 'phase3',
        'url': 'https://www.biospace.com/',
    }

    FEED_URL = 'https://feedity.com/biospace-com/WlpaV1Za.rss'
