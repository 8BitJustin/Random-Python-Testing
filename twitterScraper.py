import urllib
import urllib.request
from bs4 import BeautifulSoup

# Twitter scraper example, https://www.youtube.com/watch?v=o0RasL5uxkg&t=39s

theurl = "https://twitter.com/realDonaldTrump"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

print(soup.title.text)
for link in soup.findAll('a'):
    print(link.get('href'))
    print(link.text)