from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'globenewswire',
        'category': 'biotech',
        'url': 'https://www.globenewswire.com/',
    }

    FEED_URL = 'https://www.globenewswire.com/RssFeed/industry/4573-Biotechnology/feedTitle/GlobeNewswire%20-%20Industry%20News%20on%20Biotechnology'
