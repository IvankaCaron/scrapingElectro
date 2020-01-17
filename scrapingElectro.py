import requests
from bs4 import BeautifulSoup
import pandas as pd

dataList = []

urls = ['https://www.webscraper.io/test-sites/e-commerce/allinone/computers/laptops','https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets', 'https://www.webscraper.io/test-sites/e-commerce/allinone/phones/touch' ]
#scrape elements
for url in urls:
    electro_response = requests.get(url)
    #print(perdu_response.content)
    soup = BeautifulSoup(electro_response.content, "html.parser")

#print(f'titre de la page : {soup.title.contents[0]}') contents afiche list
#print(f'titre de la page : {soup.title.text}')

    #<h1 class="page-header">Computers / Tablets</h1>
    categorytext = soup.find_all('h1', {'class': "page-header" })
    print(categorytext[0].text)

    prix_electro = soup.find_all('h4', {'class': "price"})
#print(prix_electro[1].text)

    title_electro = soup.find_all('a', {'class': "title"})
#print(title_electro[1].text)


    listPrix = []
    listElectro = []
    listCategory = []
    for i in prix_electro:
        listPrix.append(i.text)
    for j in title_electro:
        listElectro.append(j.text)
    for c in categorytext:
        listCategory.append(c.text)

#print(listPrix)
#print(listElectro)

    print(len(listPrix))
    print(len(listElectro))
    print(len(categorytext))

    df = pd.DataFrame(list(zip(listCategory*len(listElectro), listElectro, listPrix)), columns=['Category', 'Name', 'Prix'])
    dataList.append(df)

#i = 0
#for data in dataList:
    #data.to_excel(f'laptopEtTablets{i}.xls')
    #i = i+1
    #print(data)

dfFinal = pd.concat(dataList)
#print(dfFinal)
dfFinal.to_excel('tabletEtLaptopsEtTouch.xls')


#faceplat_info = soup.find_all('div', {'class' :'c-faceplate__info' })

#print(faceplat_info)
#print(soup.find_all('span', {'class' :'c-faceplate__info' }))

#cours_eur_btc =  faceplat_info[0].find_all('span', {'class': 'c-instrument'})

#print(cours_eur_btc)
#prix_eur_btc = cours_eur_btc[0].text
#variation_eur_btc = cours_eur_btc[1].text

#print(f'le bitcoin vaut {prix_eur_btc} euros.')
#print(f'il a varie de  {variation_eur_btc} depuis matin')