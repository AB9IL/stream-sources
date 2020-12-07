from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'globenewswire',
        'url': 'https://www.globenewswire.com/',
    }

    FEED_URL = 'https://www.globenewswire.com/en/Rss/List'
