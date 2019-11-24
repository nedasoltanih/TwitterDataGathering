'''
 Getting Tweets containing a special hashtag from Twitter using Scrapy library
'''

from scrapy import settings
from scrapy import crawler
import scrapy
import re
import json
import os
import pandas as pd
from bs4 import BeautifulSoup

URL = ['https://mobile.twitter.com/hashtag/DataScience']

class FirstSpider(scrapy.Spider):
    name = "topic1"
    allowed_domains = ['www.twitter.com']

    # Initialize request
    def start_requests(self):
        yield scrapy.Request(url=URL, callback=self.parse)

    # Parse returned response
    def parse(self, response):

        # Define a dataframe to save tweets in
        tweets = pd.DataFrame(columns=['user', 'text', 'time'])

        # Each tweet is shown in a table with a class value of "tweet"
        for tweet in response.xpath('//table[@class="tweet  "]'):
            html = tweet.get()

            # Parse the html code using BeautifulSoup
            parsed_html = BeautifulSoup(html)

            # Extract fields from the html code
            user = parsed_html.body.find(
                'div', attrs={'class': 'username'}).text.strip()
            text = parsed_html.body.find(
                'div', attrs={'class': 'dir-ltr'}).text.strip()
            time = parsed_html.body.find(
                'td', attrs={'class': 'timestamp'}).text.strip()

            tweets.loc[len(tweets)] = [user, text, time]
            print(tweets.loc[len(tweets)-1])

        with open('tweets_scrapy.csv', 'a') as f:
            tweets.to_csv(f, header=False, index=False)

# Initiate a Crawling process
process = crawler.CrawlerProcess()

# Tell the scraper which spider to use
process.crawl(FirstSpider)

# Start the crawling
process.start()
