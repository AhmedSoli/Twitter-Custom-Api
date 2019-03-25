import json
from Crawler import Crawler
import logging
import multiprocessing as mp

def crawl(username):
	crawler = Crawler(operating_system = "linux")
	crawler.crawl_with_username(username)
	crawler.destroy()


# set logging setting
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
# init twitter crawler
usernames = []

# get usernames political journalists on twitter
with open("political_authors/statsocial.json","r") as f:
	journalists = json.load(f)
	# iterate over all journalists
	for journalist in journalists:
		usernames.append(journalist['username'].split("@")[-1])

p = mp.Pool(12)

p.map(crawl,usernames)
