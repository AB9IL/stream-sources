from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'businesswire',
        'url': 'https://www.businesswire.com',
    }

    FEED_URL = 'https://www.businesswire.com/portal/site/home/news/industries/'
