from firehose import Firehose

def main():
    firehose = Firehose()
    # Add ABC News
    # stream = firehose.add_source('abc.politics').stream
    # firehose.add_source('abc.technology', stream=stream)
    # firehose.add_source('abc.us', stream=stream)
    # firehose.add_source('abc.world', stream=stream)
    # firehose.add_source('abc', stream=stream)
    # Add Ars Technica
    # stream = firehose.add_source('arstechnica.business').stream
    # firehose.add_source('arstechnica.gadgets', stream=stream)
    # firehose.add_source('arstechnica.science', stream=stream)
    # firehose.add_source('arstechnica.security', stream=stream)
    # firehose.add_source('arstechnica.software', stream=stream)
    # firehose.add_source('arstechnica', stream=stream)
    # Add Axios
    # stream = firehose.add_source('axios.politics').stream
    # firehose.add_source('axios.science', stream=stream)
    # firehose.add_source('axios.technology', stream=stream)
    # firehose.add_source('axios.world', stream=stream)
    # firehose.add_source('axios', stream=stream)
    # Add BBC News
    # stream = firehose.add_source('bbc.business').stream
    # firehose.add_source('bbc.science', stream=stream)
    # firehose.add_source('bbc.technology', stream=stream)
    # firehose.add_source('bbc.world', stream=stream)
    # firehose.add_source('bbc', stream=stream)
    # Add Benzinga
    stream = firehose.add_source('benzinga.biotech').stream
    firehose.add_source('benzinga.contracts', stream=stream)
    firehose.add_source('benzinga.downgrades', stream=stream)
    firehose.add_source('benzinga.earnings', stream=stream)
    firehose.add_source('benzinga.fda', stream=stream)
    firehose.add_source('benzinga.guidance', stream=stream)
    firehose.add_source('benzinga.initiation', stream=stream)
    firehose.add_source('benzinga.offerings', stream=stream)
    firehose.add_source('benzinga.penny-stocks', stream=stream)
    firehose.add_source('benzinga.sec', stream=stream)
    firehose.add_source('benzinga.short-sellers', stream=stream)
    firehose.add_source('benzinga.small-cap-analysis', stream=stream)
    firehose.add_source('benzinga.upgrades', stream=stream)
    # Add BioSpace
    stream = firehose.add_source('biospace.approvals').stream
    firehose.add_source('biospace.earnings', stream=stream)
    firehose.add_source('biospace.phase2', stream=stream)
    firehose.add_source('biospace.phase3', stream=stream)
    firehose.add_source('biospace.products', stream=stream)
    # Add BleepingComputer
    # firehose.add_source('bleepingcomputer')
    # Add Businesswire
    stream = firehose.add_source('businesswire.airtravel').stream
    firehose.add_source('businesswire.altenergy', stream=stream)
    firehose.add_source('businesswire.biotech', stream=stream)
    firehose.add_source('businesswire.clinicaltrials', stream=stream)
    firehose.add_source('businesswire.diabetes', stream=stream)
    firehose.add_source('businesswire.diseases', stream=stream)
    firehose.add_source('businesswire.fda', stream=stream)
    firehose.add_source('businesswire.health', stream=stream)
    firehose.add_source('businesswire.maritime', stream=stream)
    firehose.add_source('businesswire.nanotech', stream=stream)
    firehose.add_source('businesswire.oilgas', stream=stream)
    firehose.add_source('businesswire.oncology', stream=stream)
    firehose.add_source('businesswire.onlineretail', stream=stream)
    firehose.add_source('businesswire.pharmaceuticeuticals', stream=stream)
    firehose.add_source('businesswire.semiconductors', stream=stream)
    firehose.add_source('businesswire.software', stream=stream)
    # Add BuzzFeed News
    # stream = firehose.add_source('buzzfeednews.politics').stream
    # firehose.add_source('buzzfeednews.technology', stream=stream)
    # firehose.add_source('buzzfeednews.world', stream=stream)
    # firehose.add_source('buzzfeednews', stream=stream)
    # Add CBS News
    # stream = firehose.add_source('cbsnews.politics').stream
    # firehose.add_source('cbsnews.technology', stream=stream)
    # firehose.add_source('cbsnews.us', stream=stream)
    # firehose.add_source('cbsnews.world', stream=stream)
    # firehose.add_source('cbsnews', stream=stream)
    # Add CNBC
    # stream = firehose.add_source('cnbc.business').stream
    # firehose.add_source('cnbc.politics', stream=stream)
    # firehose.add_source('cnbc.technology', stream=stream)
    # firehose.add_source('cnbc.us', stream=stream)
    # firehose.add_source('cnbc.world', stream=stream)
    # firehose.add_source('cnbc', stream=stream)
    # Add C-SPAN
    # firehose.add_source('cspan')
    # Add Globes
    stream = firehose.add_source('globes.aerospace').stream
    # firehose.add_source('globes.energy', stream=stream)
    firehose.add_source('globes.healthcare', stream=stream)
    firehose.add_source('globes.infotech', stream=stream)
    # Add GlobeNewswire
    stream = firehose.add_source('globenewswire.biotech').stream
    firehose.add_source('globenewswire.hardware', stream=stream)
    firehose.add_source('globenewswire.pharmaceuticals', stream=stream)
    firehose.add_source('globenewswire.semiconductors', stream=stream)
    firehose.add_source('globenewswire.software', stream=stream)
    # Add HuffPost
    # stream = firehose.add_source('huffpost.business').stream
    # firehose.add_source('huffpost.politics', stream=stream)
    # firehose.add_source('huffpost.science', stream=stream)
    # firehose.add_source('huffpost.technology', stream=stream)
    # firehose.add_source('huffpost.us', stream=stream)
    # firehose.add_source('huffpost.world', stream=stream)
    # firehose.add_source('huffpost', stream=stream)
    # Add NPR News
    # stream = firehose.add_source('npr.business').stream
    # firehose.add_source('npr.politics', stream=stream)
    # firehose.add_source('npr.science', stream=stream)
    # firehose.add_source('npr.technology', stream=stream)
    # firehose.add_source('npr.world', stream=stream)
    # firehose.add_source('npr', stream=stream)
    # Add The New York Times
    # stream = firehose.add_source('nytimes.business').stream
    # firehose.add_source('nytimes.politics', stream=stream)
    # firehose.add_source('nytimes.science', stream=stream)
    # firehose.add_source('nytimes.technology', stream=stream)
    # firehose.add_source('nytimes.us', stream=stream)
    # firehose.add_source('nytimes.world', stream=stream)
    # firehose.add_source('nytimes', stream=stream)
    # Add Politico
    # stream = firehose.add_source('politico.congress').stream
    # firehose.add_source('politico.defense', stream=stream)
    # firehose.add_source('politico.economy', stream=stream)
    # firehose.add_source('politico', stream=stream)
    # Add PR Newswire
    stream = firehose.add_source('prnewswire.businesstech').stream
    firehose.add_source('prnewswire.consumertech', stream=stream)
    firehose.add_source('prnewswire.health', stream=stream)
    # Add Reuters
    stream = firehose.add_source('reuters.business').stream
    # firehose.add_source('reuters.money', stream=stream)
    # firehose.add_source('reuters.politics', stream=stream)
    # firehose.add_source('reuters.science', stream=stream)
    firehose.add_source('reuters.sec-filings', stream=stream)
    # firehose.add_source('reuters.technology', stream=stream)
    # firehose.add_source('reuters.us', stream=stream)
    # firehose.add_source('reuters.world', stream=stream)
    # firehose.add_source('reuters', stream=stream)
    # Add Slate
    # stream = firehose.add_source('slate.business').stream
    # firehose.add_source('slate.politics', stream=stream)
    # firehose.add_source('slate.technology', stream=stream)
    # firehose.add_source('slate', stream=stream)
    # Add The Atlantic
    # stream = firehose.add_source('theatlantic.business').stream
    # firehose.add_source('theatlantic.politics', stream=stream)
    # firehose.add_source('theatlantic.science', stream=stream)
    # firehose.add_source('theatlantic.technology', stream=stream)
    # firehose.add_source('theatlantic.us', stream=stream)
    # firehose.add_source('theatlantic', stream=stream)
    # Add The Daily Beast
    # stream = firehose.add_source('thedailybeast.politics').stream
    # firehose.add_source('thedailybeast.us', stream=stream)
    # firehose.add_source('thedailybeast.world', stream=stream)
    # firehose.add_source('thedailybeast', stream=stream)
    # Add The Guardian
    # stream = firehose.add_source('theguardian.business').stream
    # firehose.add_source('theguardian.politics', stream=stream)
    # firehose.add_source('theguardian.science', stream=stream)
    # firehose.add_source('theguardian.technology', stream=stream)
    # firehose.add_source('theguardian.us', stream=stream)
    # firehose.add_source('theguardian.world', stream=stream)
    # firehose.add_source('theguardian', stream=stream)
    # Add The Hill
    # stream = firehose.add_source('thehill.administration').stream
    # firehose.add_source('thehill.house', stream=stream)
    # firehose.add_source('thehill.senate', stream=stream)
    # firehose.add_source('thehill', stream=stream)
    # Add The Intercept
    # firehose.add_source('theintercept')
    # Add The New Yorker
    # stream = firehose.add_source('thenewyorker.technology').stream
    # firehose.add_source('thenewyorker', stream=stream)
    # Add Threatpost
    # firehose.add_source('threatpost')
    # Add USA Today
    # stream = firehose.add_source('usatoday.national').stream
    # firehose.add_source('usatoday.washington', stream=stream)
    # firehose.add_source('usatoday.world', stream=stream)
    # firehose.add_source('usatoday', stream=stream)
    # Add VICE
    # stream = firehose.add_source('vice.business').stream
    # firehose.add_source('vice.politics', stream=stream)
    # firehose.add_source('vice.science', stream=stream)
    # firehose.add_source('vice.technology', stream=stream)
    # firehose.add_source('vice', stream=stream)
    # Add Vox
    # stream = firehose.add_source('vox.business').stream
    # firehose.add_source('vox.politics', stream=stream)
    # firehose.add_source('vox.technology', stream=stream)
    # firehose.add_source('vox.world', stream=stream)
    # firehose.add_source('vox', stream=stream)
    # Add Washington Post
    # stream = firehose.add_source('washingtonpost.business').stream
    # firehose.add_source('washingtonpost.national', stream=stream)
    # firehose.add_source('washingtonpost.politics', stream=stream)
    # firehose.add_source('washingtonpost.technology', stream=stream)
    # firehose.add_source('washingtonpost.world', stream=stream)
    # firehose.add_source('washingtonpost', stream=stream)
    # Add Wired
    # stream = firehose.add_source('wired.business').stream
    # firehose.add_source('wired.science', stream=stream)
    # firehose.add_source('wired.security', stream=stream)
    # firehose.add_source('wired', stream=stream)
    # Start firehose
    firehose.start()


if __name__ == '__main__':
    main()
