import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url ="https://en.wikipedia.org/wiki/Python_(programming_language)"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
   
    soup= BeautifulSoup(response.text,'html.parser')
    
    images= soup.find_all('img')
    
    print (f"Found {len(images)} images on {url}\n")
    
    for i, img in enumerate(images,start=1):
        img_url= img.get("src")
        alt_text=img.get('alt','No alt text')   
        
        if img_url and not img_url.startswith('http'):
            img_url=urljoin(url,img_url)
            
            print(f"Image {1}:")
            print(f"URL: {img_url}")
            print(f"Alt text : {alt_text}\n")
            
except requests.RequestException as e:
    print(f"Error fetching the page:{e}") 
   
    