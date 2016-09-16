import requests
import time 
import main_script_file 

pg_no=0
base_url="https://www.google.co.in/search"
keyword=('QA team') # Kewyword to scrap data for
payload = {'q': keyword, 'start': pg_no}

data=main_script_file.GenerateHtml(base_url,payload)
final_data=main_script_file.parsing_and_scrape_data(data)
#main_script_file.write_on_csv(final_data)

"""pg_no=0 
total_pages=10 #This number of pages it will scrap data

while pg_no<=total_pages: 
	base_url="https://www.google.co.in/search"
	keyword=('where am i') # Kewyword to scrap data for
	payload = {'q': keyword, 'start': pg_no}
	#headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
	
	raw_data=main_script_file.raw_data_generate_html_from_provided_url(base_url,payload)
	print(raw_data)

	pg_no=10+pg_no
	time.sleep(60)
"""

	
