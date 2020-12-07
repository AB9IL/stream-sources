from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'globenewswire',
        'category': 'software',
        'url': 'https://www.globenewswire.com/',
    }

    FEED_URL = 'https://www.globenewswire.com/RssFeed/industry/9537-Software/feedTitle/GlobeNewswire%20-%20Industry%20News%20on%20Software'
