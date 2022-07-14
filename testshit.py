#import requests
#URL = "https://www.google.com/search?q=euro+to+usd"
#r = requests.get(URL)
#print(r.content)
#dDoNo ikb4Bb gsrt GDBPqd

import requests
import random
from bs4 import BeautifulSoup
  
URL = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=USD"
fake_id = random.randint(1000,9999)
fake_id_string = str(fake_id)
r = requests.get(URL,params={"id":fake_id_string, "availability":"available"})
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
table = soup.find('p', attrs = {'class':'result__BigRate-sc-1bsijpp-1 iGrAod'})
txt = table.get_text()
print(table)
print(txt)