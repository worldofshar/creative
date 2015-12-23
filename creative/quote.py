from requests import get
from lxml import html
from datetime import date, timedelta


def word_of_the_day():
    page = get("http://dictionary.reference.com/wordoftheday/")
    tree = html.fromstring(page.content)
    day = str(date.today() - timedelta(days=1))
    word = tree.xpath('//*[@id="wotd-' + day +
                      '"]/div[2]/div[1]/div/div[3]/div/strong')[0].text
    defn = tree.xpath('//*[@id="wotd-' + day +
                      '"]/div[2]/div[1]/div/div[3]/ol/li/span')[0].text
    return {'w': word, 'd': defn}


def quote_of_the_day():
    page = get("https://www.goodreads.com/quotes")
    tree = html.fromstring(page.content)
    quote = tree.xpath('//*[@id="quoteoftheday"]/div[1]/i')[0].text
    author = tree.xpath('//*[@id="quoteoftheday"]/div[2]/strong/div/a')[0].text
    return {'q': quote, 'a': author}
