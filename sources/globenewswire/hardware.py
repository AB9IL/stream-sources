from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'globenewswire',
        'category': 'hardware',
        'url': 'https://www.globenewswire.com/',
    }

    FEED_URL = 'https://www.globenewswire.com/RssFeed/industry/9572-Computer%20Hardware/feedTitle/GlobeNewswire%20-%20Industry%20News%20on%20Computer%20Hardware'
