#  scrape a particular section/ data from the hackernews website
# tool used- BEAUTIFULSOUP
import requests
from bs4 import BeautifulSoup
import pprint

res=requests.get('https://news.ycombinator.com/')
# print(res) if everything is alright then you will get response 200
soup=BeautifulSoup(res.text,'html.parser')
# print(soup.body)
# print(soup.findAll('a'))   this will give all the a tags as output
# using css selectors
# print(soup.select('.score')) this will give you all the span tags actua;ly which have class name as score.

#grab all storylinks in a list
links=soup.select('.storylink') 
 # grab all the span tags with score class
subtext=soup.select('.subtext') 
# '.' represent a class in css!! (NOTE)

def custom_hackNews(links,subtext):
    hn=[]
    for idx, link in enumerate(links):
        title= link.getText()
        href=links[idx].get('href',None)
        vote=subtext[idx].select('.score')
        if len(vote):
            score=int(vote[0].getText().replace(' points',''))
            if score> 100:
                hn.append({'title': title,'link': href,'score': score})
    return sorted(hn,key=lambda k: k['score'],reverse=True)

pprint.pprint(custom_hackNews(links,subtext))