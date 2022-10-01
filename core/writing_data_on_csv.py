"""writing data to the csv"""
from bs4 import BeautifulSoup
RAW_DATA = ""
soup = BeautifulSoup(RAW_DATA, "html.parser")
ParserData = {
  "HeaderDivHtml": (soup.find_all('div', {"class": "graybar"})),
  "MainContentDivHtml": (soup.find_all('div', {"class": "sitemap-menu-box"})),
  "FooterDivHtml": (soup.find_all('div', {"class": "footer-band-align"})),
  "SocialDivHtml": (soup.find_all('div', {"class": "bottomfooter-align"})),
  }
RESEOURCE_URL = 'http://stackoverflow.uk.co/questions/339537/'
new = RESEOURCE_URL.rsplit('//', maxsplit=1)[-1].split("/")[0]
print(new)
