import logging
import argparse, sys
from Crawler import Crawler


# set logging setting
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--username', help='Enter the username of the person you want to crawl', type=str, default="AltumAlien")
parser.add_argument('--os', help='Enter the name of the operating system (win: windows, mac: mac os, linux: linux', type=str, default="mac")
args = parser.parse_args()

crawler = Crawler(operating_system = args.os)
crawler.crawl_with_username(username= args.username)
crawler.destroy()