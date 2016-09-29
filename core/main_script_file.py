import csv
import os.path
import builtwith

<<<<<<< HEAD:core/main_script_file.py
def generate_html(base_url,payload):
	'''
	In this function request is sent and html reponse
	is recorded in html_doc
	'''

	r = requests.get(base_url, params=payload)
	print ("Your'r on" ,r.url)
	html_doc= (r.content)
	return html_doc	

def parsing_data(raw_data):
		
		
		soup = BeautifulSoup(raw_data,'html.parser')
		g_data= (soup.find_all('div',{"class":"g"}))
		
		for items in g_data:
			product_details={}
			atag= items.a
			cite= items.cite
			title = (atag.text)
			link=(cite.text)
			print (link)
			links=strip_url_to_domain(link)
			print (links)
			product_details["Title"]=title
			product_details["Links"]=links
			write_on_csv(product_details)
		
		
def write_on_csv(data):

	file_exists = os.path.isfile('googleresults.csv')
	with open ('googleresults.csv', 'a',newline='') as csvfile:
		fieldnames = ['Title', 'Links']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		if not file_exists:
			writer.writeheader()
		
		writer.writerow(data)
		print ('wrote on to the file')

def strip_url_to_domain(urls):
    link= urls.split("//")[-1].split("/")[0]
    links= link
    return links

def get_data_builtwith(links):
	website = builtwith.parse(links)
	print (website)
=======
import requests
from bs4 import BeautifulSoup


FIELD_TITLE = "Title"
FIELD_LINKS = "Links"


def fetch_html(url, payload):
    """Fetch url and return the HTML content"""
    r = requests.get(url, params=payload)
    print("You're on", r.url)
    return r.content


def parse_and_scrape_data(raw_data):
    soup = BeautifulSoup(raw_data, "html.parser")

    for item in soup.find_all("div", {"class": "g"}):
        title = item.a.text
        links = item.cite.text
        print(links)
        product_details = {
            FIELD_TITLE: title,
            FIELD_LINKS: links,
        }
        write_on_csv(product_details)


def write_on_csv(product_details, filename="googleresults.csv"):
    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=(FIELD_TITLE, FIELD_LINKS))

        if not file_exists:
            writer.writeheader()

        writer.writerow(product_details)
        print("wrote on to the file")


if __name__ == "__main__":
    print("Running as a progam")
    # TODO: Do something useful
>>>>>>> refs/remotes/origin/master:main_script_file.py
