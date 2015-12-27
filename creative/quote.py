from requests import get
from lxml import html


def word_of_the_day():
    page = get("http://www.oxforddictionaries.com/")
    tree = html.fromstring(page.content)
    w_xpath = '/html/body/div[3]/div/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div/div/a/span[2]'
    d_xpath = '/html/body/div[3]/div/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div/div/a/div[1]/div[3]'
    word = tree.xpath(w_xpath)[0].text

    defn = tree.xpath(d_xpath)[0].text
    return {'w': word, 'd': defn}


def quote_of_the_day():
    page = get("https://www.goodreads.com/quotes")
    tree = html.fromstring(page.content)
    quote = tree.xpath('//*[@id="quoteoftheday"]/div[1]/i')[0].text
    author = tree.xpath('//*[@id="quoteoftheday"]/div[2]/strong/div/a')[0].text
    return {'q': quote, 'a': author}
