import time
import json
import logging
from Browser import Browser
from selenium.webdriver.common.keys import Keys


class Crawler:

	def __init__(self):
		self.browser = Browser()

	def scroll_till_bottom(self):

		logging.info("Started scrolling....")

		while True:
			# get page height
			page_height = self.browser.session.execute_script("return document.body.scrollHeight")
			# scroll till the bottom of the page
			self.browser.session.execute_script("window.scrollTo(0, document.body.scrollHeight)")
			# wait for 1 seconds
			time.sleep(1)
			# get new page height
			new_page_height = self.browser.session.execute_script("return document.body.scrollHeight")
			# if new height equals old height then bottom is reached
			if new_page_height == page_height:
				break
		
		logging.info("Finished scrolling....")

	def extract_tweets(self,posts,username):

		tweets = []

		for key,post in enumerate(posts):
			try:
				tweet = {}
				tweet['text'] = post.find_element_by_class_name("tweet-text").text
				tweet['timestamp'] = post.find_element_by_class_name("tweet-timestamp").get_attribute('title')
				tweet['retweet_count'] =  post.find_element_by_class_name("ProfileTweet-action--retweet").find_element_by_class_name("ProfileTweet-actionCount").get_attribute('data-tweet-stat-count')
				tweet['favorite_count'] =  post.find_element_by_class_name("ProfileTweet-action--favorite").find_element_by_class_name("ProfileTweet-actionCount").get_attribute('data-tweet-stat-count')
				tweet['author'] = post.find_element_by_class_name("username").find_element_by_tag_name("b").text
				if tweet['author'] != 'HillaryClinton':
					tweet['is_retweet'] = True
				else:
					tweet['is_retweet'] = False

				tweets.append(tweet)
				if key % 100 == 0:
					logging.info("{} tweets imported from {}".format(key,username)) 
			except Exception as e:
				print(e)

		return tweets

	def crawl_with_username(self,username,date_from = "2006-01-01",date_to = "2030-01-01"):

		logging.info("Crawling user: {} from: {} to: {}".format(username,date_from,date_to))
		# use twittet advanced search to retrieve all tweets
		advanced_search_link = "https://twitter.com/search?f=tweets&q=from%3A" + username + "%20since%3A" + date_from + "%20until%3A" + date_to + "&src=typd"
		self.browser.session.get(advanced_search_link)
		time.sleep(1)
		# scroll till bottom of the page and load all content
		self.scroll_till_bottom()

		posts = self.browser.session.find_elements_by_class_name("content")
		
		tweets = self.extract_tweets(posts,username)

		self.generate_json(tweets,username,date_from,date_to)

	def generate_json(self,tweets,username,date_from,date_to):
		with open(username + "_tweets_" + date_from + "_" + date_to + ".json","w+") as f:
			json.dump(tweets,f)
			print("Tweets crawled:",len(tweets))

	def destroy(self):
		self.browser.quit();

