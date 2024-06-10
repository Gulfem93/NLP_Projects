import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.yelp.com/biz/kia-of-marin-novato")

print(r.status_code)

soup = BeautifulSoup(r.text, "html.parser")

soup_lis = soup \
 .find('ul', {'class': 'list__09f24__ynIEd'})\
 .find_next('li', {'class': 'y-css-1jp2syp'})\


review =  []
reviews =  []
 
for lis in soup_lis:
    li = lis.find_next("div", {'class': 'y-css-1iy1dwt'})\
        .find_next("div", {'class': 'y-css-cluvhg'})\
        .find_next("p", {'class': 'comment__09f24__D0cxf y-css-h9c2fl'})\
        .find_all_next("span", {'class': 'raw__09f24__T4Ezm'})
        
    for l in li:
        reviews.append(l.get_text)
        print("------------------")
        print(l.get_text)

#print(reviews)
