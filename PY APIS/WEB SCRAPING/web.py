import requests
from bs4 import BeautifulSoup
import csv

url="https://www.bikewale.com/royalenfield-bikes/"
# url="https://www.flipkart.com/?s_kwcid=AL!739!3!538013715273!e!!g!!%E0%A4%AB%E0%A5%8D%E0%A4%B2%E0%A4%BF%E0%A4%AA%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%9F&gclsrc=aw.ds&semcmpid=sem_8024046704_brand_hindi_nc_goog&ef_id=Cj0KCQjw3vO3BhCqARIsAEWblcCGWYHrLxAxlxThh7J8BmqPmFEN3rHluAC_7A0vOVAjQat0GLRZxCAaAhbSEALw_wcB:G:s&s_kwcid=AL!739!3!705840437232!!!g!!&gclsrc=aw.ds&&cmpid=sem_4972523958_grocery_Search_ON/NC_DSA_Session&gad_source=1&gclid=Cj0KCQjw3vO3BhCqARIsAEWblcCGWYHrLxAxlxThh7J8BmqPmFEN3rHluAC_7A0vOVAjQat0GLRZxCAaAhbSEALw_wcB"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
# print(soup.text) # text

# image=soup.findAll('h2')
# for i in image:
#     print(i.text)

# find a single
# header=soup.find('h1')
# print(header.text)

# links
links=soup.find_all('a')
# for links in links:
#     print(links.get('href'))

#attributes of an element
# first_link=links[10]
# print(first_link.text)

# get text from all links
# for i in links:
#     print(i.text)

# get links
# for i in links:
#     print(i.get('href'))

ls=set()
# get class list
# for i in soup.find_all(class_=True):
#     ls.update(i['class'])
# for i in ls:
#     print(i)