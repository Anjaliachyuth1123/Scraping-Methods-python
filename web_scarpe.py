#import required modules
import requests
#get url
page =requests.get("https://en.wikipedia.org/wiki/Main_Page")

#diaplay status code
print(page.status_code
      )

#display scraped data
print(page.content)

#import  required modules
from bs4 import BeautifulSoup
import requests

#get Url
page=requests.get("https://en.wikipedia.org/wiki/Main_Page")

#scraped webpage
soup=BeautifulSoup(page.content,'html.parser')

#display scraped data
print(soup.prettify())

from bs4 import BeautifulSoup
import requests

#get url
page=requests.get("https://en.wikipedia.org/wiki/Main_Page")

#scrape webpage
soup = BeautifulSoup(page.content,'html.parser')

list(soup.children)

#find all occurence of p in html
#includes html tages
print(soup.find_all('p'))

print('n\n')

#return only text
#does not inclue html tages
print (soup.find_all('p')[0].get_text())

#scrape webpage
soup= BeautifulSoup(page.content,'html.parser')

#create object
object=soup.find(id="mp-left")

#find tags
items=object.find_all(class_="mp-h2")
result= items[0]

#display tags
print(result.prettify())

