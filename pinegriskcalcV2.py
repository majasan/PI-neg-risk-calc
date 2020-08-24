
import requests
import urllib3
import re

conNumber = input('Enter Contract Number := ')
urlMarket = 'https://www.predictit.org/api/marketdata/markets/'+conNumber
response = requests.get(urlMarket)
print(urlMarket)
with open('/users/jamundur/Downloads/feedv3.txt','wb') as file:
    file.write(response.content)
psum=0.0
regexp = re.compile(r'      "bestSellYesCost".*?([0-9.-]+)') 
with open('/users/jamundur/Downloads/feedv3.txt') as file:
    for line in file:
        match = regexp.match(line)
        if match:
            psum=psum+float(match.group(1))  
      
print(" Total of all comes to :",round(psum,2))
if psum >= 1.10 :
    print( "This contract is ready for Negative Risk betting. Bet equal cash on all contracts within the market. Good luck !!!")
else :
    print(" This market and contracts are NOT ready for Negative Risk betting.")
