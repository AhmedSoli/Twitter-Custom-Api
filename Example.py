import logging
from Crawler import Crawler

# set logging setting
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

crawler = Crawler()
crawler.crawl_with_username(username="realDonaldTrump")
crawler.destroy()