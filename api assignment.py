import requests
import pandas as pd

url = "https://content.guardianapis.com/search?api-key=test&q=Nigeria&page-size=100&from-date=2025-01-01"

response = requests.get(url)
response.status_code


data= response.json()



result= data['response']['results']

codeurl1=[]

for url in result:
    codeurl1.append(url['webUrl'])
print(codeurl1)

df =pd.DataFrame({'Url':codeurl1})

print(df)

df.to_csv('Nigeria.csv')
    
    