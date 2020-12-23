from sources.reuters._source import ReutersSource


class Source(ReutersSource):

    SOURCE = {
        'name': 'Reuters',
        'category': 'sec-filings',
        'url': 'https://www.reuters.com',
    }

    FEED_URL = 'https://ir.thomsonreuters.com/rss/sec-filings.xml?items=15'
