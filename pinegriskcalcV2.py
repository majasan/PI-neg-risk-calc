import requests; import urllib3; import re; import sys
urlMarket = 'https://www.predictit.org/api/marketdata/all/'
response = requests.get(urlMarket)
with open('/users/jamundur/Downloads/feedAll.txt','wb') as file:
    file.write(response.content)
regexp1 = re.compile(r'      "id".*?([0-9.-]+)') 
regexp2 = re.compile(r'          "bestSellYesCost".*?([0-9.-]+)') 
regexp3 = re.compile(r'      "timeStamp".*?([0-9.-]+)')
regexp4 = re.compile(r'      "name".*?([0-9.-]+)')
print("""
******************************************************************************
\tThis program will print all contracts ( and their links) that are eligible
for betting with no or negative risk.
\tPlease read about it from Zvi Bodie at the link below. 
\thttps://www.lesswrong.com/posts/qzRzQgxiZa3tPJJg8/free-money-at-predictit
*******************************************************************************
""")
psum = 0.0;finalsum = 0.0
with open('/users/jamundur/Downloads/feedAll.txt') as file:
    for line in file:
        match1 = regexp1.match(line); match2 = regexp2.match(line) ; match3 = regexp3.match(line)
        psum=0.0
        if match1:
            cid = match1.group(1)  
        if match2:
            psum=psum+float(match2.group(1))
            finalsum=finalsum+psum
        if match3:
            if round(finalsum,2) >=1.11:
                print("\n\t\thttps://www.predictit.org/markets/detail/"+cid,"\t ",round(finalsum,2),"\n")
            finalsum=0.0

print("""
*******************************************************************************
\tMake sure you buy *equal* number of 'Buy No' contracts in *all* tranches for each 
of the above contracts. 
\tPlease read more before you play this betting strategy where you get paid 
to bet !!!
https://blog.rossry.net/predictit/
*******************************************************************************
""")
### Jasan Mundur and Hari Krishnan
