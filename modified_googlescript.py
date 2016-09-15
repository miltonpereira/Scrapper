import requests
import time 
import oops_script

pg_no=0 
total_pages=10 #This number of pages it will scrap data
while pg_no<=total_pages: 
	base_url="https://www.google.co.in/search"
	keyword=('Dev Companies') # Kewyword to scrap data for
	payload = {'q': keyword, 'start': pg_no}
	#headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

	def generate_user_input():
		print (pg_no)
		r = requests.get(base_url, params=payload)
		print (r.url)
		html_doc= (r.content)
		return html_doc	
			
	raw_data=generate_user_input()
	product=oops_script.scrape_data(raw_data)
	pg_no=10+pg_no
	time.sleep(60)


	
