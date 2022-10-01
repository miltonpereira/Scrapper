"""load the csv file"""
__author__ = 'BackOffice-3'
with open("url.csv", "r", encoding="utf-8") as f:
    lines = f.read()
    lines = lines.replace("http://", "")
    lines = lines.replace("https://", "")
    lines = lines.replace("www.", "")
    urls = [url.split('/')[0] for url in lines.split()]
    print('\n'.join(urls))
