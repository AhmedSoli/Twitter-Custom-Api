from Browser import Browser
from json import dump
# url to all_slides which provides a list of most popular political 
# authors in the US and gives an estimation on how left-leaning or 
# right-leaning they are

url = "https://www.allsides.com/media-bias/media-bias-ratings?field_featured_bias_rating_value=All&field_news_source_type_tid%5B1%5D=1&field_news_bias_nid%5B2%5D=2&field_news_bias_nid%5B3%5D=3&field_news_bias_nid%5B4%5D=4&title=&customFilter=1"
browser = Browser(operating_system="mac")

people = []

while (True):
	print(url)
	browser.session.get(url)			
	rows = browser.session.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")

	for key,row in enumerate(rows):
		person = {}

		try:
			person['name'] = row.find_element_by_class_name("source-title").find_element_by_tag_name("a").text
			person['bias'] = row.find_element_by_class_name("views-field-field-bias-image").\
			find_element_by_tag_name("a").find_element_by_tag_name("img").get_attribute("title").split(":")[1].replace(" ","")
			person['community_feedback'] = row.find_element_by_class_name("community-feedback-rating-page").text
			person['agree'] = row.find_element_by_class_name("community-feedback").find_element_by_class_name("agree").text
			person['disagree'] = row.find_element_by_class_name("community-feedback").find_element_by_class_name("disagree").text
			people.append(person)
			print("{} added".format(person['name']))
		except Exception as e:
			print(e)

	next = browser.session.find_elements_by_class_name("pager-next")
	if len(next) > 0:
		url = next[0].find_element_by_tag_name("a").get_attribute("href")
	else:
		print("Saving collected data")
		with open('political_authors/allsides.json','w+') as f:
			dump(people,f)
			break