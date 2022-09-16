from bs4 import BeautifulSoup
raw_data = ""
soup = BeautifulSoup(raw_data, "html.parser")
ParserData = {
  "HeaderDivHtml": (soup.find_all('div', {"class": "graybar"})),
  "MainContentDivHtml": (soup.find_all('div', {"class": "sitemap-menu-box"})),
  "FooterDivHtml": (soup.find_all('div', {"class": "footer-band-align"})),
  "SocialDivHtml": (soup.find_all('div', {"class": "bottomfooter-align"})),
  }
url = 'http://stackoverflow.uk.co/questions/339537/'
new = url.split("//")[-1].split("/")[0]
print(new)
