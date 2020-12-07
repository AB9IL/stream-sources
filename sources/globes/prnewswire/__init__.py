from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'prnewswire',
        'url': 'https://www.prnewswire.com',
    }

    FEED_URL = 'https://www.prnewswire.com/rss/'
