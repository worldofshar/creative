from requests import get
from lxml import html


def word_of_the_day():
    page = get("http://www.oed.com/")
    tree = html.fromstring(page.content)
    w_xpath = '//*[@id="columnTwo"]/div[3]/div/div/p[1]/a/span/span[1]'
    d_xpath = '//*[@id="columnTwo"]/div[3]/div/div/p[3]'
    word = tree.xpath(w_xpath)[0].text

    defn = tree.xpath(d_xpath)[0].text
    return {'w': word, 'd': defn}


def quote_of_the_day():
    page = get("https://www.goodreads.com/quotes")
    tree = html.fromstring(page.content)
    quote = tree.xpath('//*[@id="quoteoftheday"]/div[1]/i')[0].text
    author = tree.xpath('//*[@id="quoteoftheday"]/div[2]/strong/div/a')[0].text
    return {'q': quote, 'a': author}
