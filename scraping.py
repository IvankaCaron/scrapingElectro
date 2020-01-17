import requests
from bs4 import BeautifulSoup

cours_bitcoin_response = requests.get('https://www.boursorama.com/bourse/devises/cryptomonnaies-bitcoin-euro-BTC-EUR/')
#print(perdu_response.content)
soup = BeautifulSoup(cours_bitcoin_response.content, "html.parser")

#print(f'titre de la page : {soup.title.contents[0]}') contents afiche list
#print(f'titre de la page : {soup.title.text}')
faceplat_info = soup.find_all('div', {'class' :'c-faceplate__info' })

#print(faceplat_info)
#print(soup.find_all('span', {'class' :'c-faceplate__info' }))

cours_eur_btc =  faceplat_info[0].find_all('span', {'class': 'c-instrument'})

print(cours_eur_btc)
prix_eur_btc = cours_eur_btc[0].text
variation_eur_btc = cours_eur_btc[1].text

print(f'le bitcoin vaut {prix_eur_btc} euros.')
print(f'il a varie de  {variation_eur_btc} depuis matin')
