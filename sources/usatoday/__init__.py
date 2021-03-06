from sources.usatoday._source import UsaTodaySource


class Source(UsaTodaySource):

    SOURCE = {
        'name': 'USA Today',
        'url': 'https://www.usatoday.com',
    }

    FEED_URL = 'http://rssfeeds.usatoday.com/usatoday-newstopstories&x=1'
