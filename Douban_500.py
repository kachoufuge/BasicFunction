import bs4
import requests
from bs4 import BeautifulSoup
headers={
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15'
}
response = requests.get(f'https://movie.douban.com/top250?', headers=headers)
html=response.text
soup=BeautifulSoup(html,"html.parser")
all_titles=soup.findAll("span",attrs={"class":"title"})
for title in all_titles:
    if "/" not in title.string:
        print(title.string)