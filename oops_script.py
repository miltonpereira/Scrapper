from bs4 import BeautifulSoup
import csv
import datetime




#Please don't Modifying anything in this file, this file contains code which scraps data and inserts into csv file. 
def scrape_data(raw_data):

		product_details={}
		with open('googleresults.csv', 'a',newline='') as csvfile:
			fieldnames = ['Title', 'Links']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
		
			soup = BeautifulSoup(raw_data,'html.parser')
			#print(soup.prettify())
			g_data= (soup.find_all('div',{"class":"g"}))

			for items in g_data:
				atag= items.a
				cite= items.cite
				title = (atag.text)
				link=(cite.text)
				print (link)
				product_details["Title"]=title
				product_details["Links"]=link
				writer.writerow(product_details)



				print ("888888888888888888888888888888888888888888888888888888" , product_details)
				#print (link.prettify())
				

				





    




	



