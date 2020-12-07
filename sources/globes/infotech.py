from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'globes',
        'category': 'infotech',
        'url': 'https://www.globes.co.il/en/',
    }

    FEED_URL = 'https://www.globes.co.il/WebService/Rss/RssFeeder.asmx/FeederKeyword?iID=1376'
