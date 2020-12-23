from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'biospace',
        'url': 'https://www.biospace.com',
    }

    FEED_URL = 'https://www.biospace.com/staticpages/10283/rss-feeds/'
