from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'prnewswire',
        'category': 'consumertech',
        'url': 'https://www.prnewswire.com/',
    }

    FEED_URL = 'https://www.prnewswire.com:443/rss/consumer-technology-latest-news/consumer-technology-latest-news-list.rss'
