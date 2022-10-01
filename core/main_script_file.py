"""Main script of the scraper program"""
import csv
import os.path
import requests
from bs4 import BeautifulSoup


FIELD_TITLE = "Title"
FIELD_LINKS = "Links"


def fetch_html(url, payload):
    """Fetch url and return the HTML content"""
    make_request = requests.get(url, params=payload, timeout=10)
    print("You're on", make_request.url)
    return make_request.content


def parse_and_scrape_data(raw_data):
    '''Process the data to be scraped'''
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
    return write_on_csv


def write_on_csv(product_details, filename="googleresults.csv"):
    """Save the data to the csv file"""
    file_exists = os.path.isfile(filename)

    with open(filename, "a", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=(FIELD_TITLE, FIELD_LINKS))

        if not file_exists:
            writer.writeheader()

        writer.writerow(product_details)
        print("wrote on to the file")


if __name__ == "__main__":
    print("Running as a progam")
