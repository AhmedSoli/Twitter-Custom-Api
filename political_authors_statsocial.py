from Browser import Browser
from json import dump
# url to statsocial which provides a list of most popular political 
# authors in the US and gives an estimation on how left-leaning or 
# right-leaning they are

url = "https://www.statsocial.com/social-journalists-entire-list/"
browser = Browser(operating_system="mac")
browser.session.get("https://www.statsocial.com/social-journalists-entire-list/")

people = [] 

for row in browser.session.find_elements_by_tag_name("tr")[1:]:
	
	person = {
		"rank": row.find_element_by_class_name("inv-table-rank").text,
		"name": row.find_element_by_class_name("inv-table-name").text.split("(")[0][:-1],
		"username": row.find_element_by_class_name("inv-table-name").text.split("(")[1][:-1],
		"twitter_link": row.find_element_by_class_name("inv-table-name").find_element_by_tag_name("a").get_attribute("href"),
		"adjusted_pull": row.find_element_by_class_name("inv-table-company").text,
		"followers": row.find_element_by_class_name("inv-table-pull").text,
		"left": row.find_element_by_class_name("inv-table-followers").text,
		"right": row.find_element_by_class_name("inv-table-connections").text
	}

	people.append(person)

	print("{}:{} added".format(person['rank'],person['name']))

with open("political_authors/statsocial.json","w+") as f:
	dump(people,f)
