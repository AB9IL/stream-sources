from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'prnewswire',
        'category': 'health',
        'url': 'https://www.prnewswire.com/',
    }

    FEED_URL = 'https://www.prnewswire.com:443/rss/health-latest-news/health-latest-news-list.rss'
