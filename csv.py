import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://www.thewhiskyexchange.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
productlinks = []
t={}
data=[shampoo,whisky,soap,cream,oil,perfume,gel]
c=0
for x in range(1,6):
    k = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={}&psize=24&sort=pasc'.format(x)).text
    soup=BeautifulSoup(k,'html.parser')
    productlist = soup.find_all("li",{"class":"product-grid__item"})


    for product in productlist:
        link = product.find("a",{"class":"product-card"}).get('href')
        productlinks.append(baseurl + link)


for link in productlinks:
    f = requests.get(link,headers=headers).text
    hun=BeautifulSoup(f,'html.parser')

    try:
        price=hun.find("p",{"class":"product-action__price"}).text.replace('\n',"")
    except:
        price = None

    try:
        details=hun.find("div",{"class":"product-main__description"}).text.replace('\n',"")
    except:
        details=None

    try:
        category = hun.find("div",{"class":"product_category"}).text.replace('\n',"")
    except:
        category=None

    try:
        name=hun.find("h1",{"class":"product-main__name"}).text.replace('\n',"")
    except:
        name=None

    whisky = {"name":name,"price":price,"category":category,"details":details}

    data.append(whisky)
    c=c+1
    print("completed",c)

    shampoo = {"name":name,"price":price,"category":category,"details":details}

    data.append(shampoo)
    c=c+1
    print("completed",c)

    soap = {"name":name,"price":price,"category":category,"details":details}

    data.append(soap)
    c=c+1
    print("completed",c)

    oil = {"name":name,"price":price,"category":category,"details":details}

    data.append(oil)
    c=c+1
    print("completed",c)

    cream = {"name":name,"price":price,"category":category,"details":details}

    data.append(cream)
    c=c+1
    print("completed",c)

    perfume = {"name":name,"price":price,"category":category,"details":details}

    data.append(perfume)
    c=c+1
    print("completed",c)

df = pd.DataFrame(data)

print(df)
