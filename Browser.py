import os
from selenium import webdriver
import logging

class Browser:
	# operating systems: linux: Linux, win: Windows, mac: MAC OS
	def __init__(self,operating_system):
		# init logging
		# get path to working directory
		path = os.path.join(os.getcwd(),"chrome_driver")
		# init browser options object
		options = webdriver.ChromeOptions()
		# disable loading of images
		prefs = {"profile.managed_default_content_settings.images": 2}
		# add setting to browser
		options.add_experimental_option("prefs", prefs)
		# make chrome headless
		options.add_argument('headless')
		# start a new session using web driver
		self.session = webdriver.Chrome(os.path.join(path,operating_system),options=options)
		logging.info("Browser session started...")

	def quit(self):
		# quit browser session
		logging.info("Browser session quitting...")
		self.session.quit()
