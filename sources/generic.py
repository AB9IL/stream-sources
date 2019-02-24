from bs4 import BeautifulSoup
import feedparser
import time

from sources import Source


class FeedSource(Source):

    '''
    A generic FeedSource baseclass implements a Source class for RSS feeds.

    Classes that inherit from FeedSource should have their own FEED_URL (an RSS
    feed URL) and SOURCE (the source name) class properties.
    '''

    def update(self):
        feed = feedparser.parse(self.FEED_URL)
        entries = feed['entries']
        for entry in reversed(entries):
            url = entry['link']
            if url in self.stream:
                continue
            update = {}
            update['url'] = url
            update['title'] = clean_html(entry['title'])
            update['body'] = clean_html(entry['summary'])
            thumb = _extract_thumb(entry)
            if thumb:
                update['thumb'] = thumb
            raw_date = entry['published_parsed']
            update['date'] = time.strftime('%Y-%m-%d %H:%M:%S', raw_date)
            update['source'] = self.SOURCE
            self.stream.push(update)


def clean_html(raw):
    return BeautifulSoup(raw, 'html.parser').get_text().strip()

def _extract_thumb(entry):
    if 'media_thumbnail' in entry and len(entry['media_thumbnail']) > 0:
        return entry['media_thumbnail'][0]['url']
    if 'media_content' in entry and len(entry['media_content']) > 0:
        return entry['media_content'][0]['url']
    if 'links' in entry and len(entry['links']) > 0:
        imgs = [x for x in entry['links'] if 'image' in x['type']]
        if len(imgs) > 0:
            return imgs[0]['href']
    soup = BeautifulSoup(entry['summary'], 'html.parser')
    img = soup.find('img')
    if img:
        return img['src']
    return None
