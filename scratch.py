#beutiful soup clearify the structure of html code + access some info
#replit installs libraries automatically

import requests
from bs4 import BeautifulSoup

SiteENSH = 'https://www.ensh.dz/category/marches-publiques/'
HtmlText= requests.get(SiteENSH)
#status code => indicates if the import of request was successful
print ('status code' , HtmlText.status_code)
#HtmlText.text contains all html code in website
#print ('output', HtmlText.text[:1000])
#save file as HTML to inspect it later
with open('ENSH.html', 'w') as f:
  f.write(HtmlText.text)
#import beutiful soup to structure code better (plus lisible)
soup = BeautifulSoup(HtmlText.text, 'html.parser')

print('Page title:', soup.title.text)

#since request only excutes the html text in HtmlText= requests.get(SiteENSH) and doesnt excute the JS code cause it doesnt contain a browser we should connect it to one simulate a headless fakebrowser to run JS on the page , to do that use selinum: selinum automates browsers 
#request comes with chrome and chrome driver preinstalled 
