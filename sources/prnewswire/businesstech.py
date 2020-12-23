from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'prnewswire',
        'category': 'businesstech',
        'url': 'https://www.prnewswire.com/',
    }

    FEED_URL = 'https://www.prnewswire.com:443/rss/business-technology-latest-news/business-technology-latest-news-list.rss'
