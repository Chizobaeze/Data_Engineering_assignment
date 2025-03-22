import requests 

url= "http://api.football-data.org/v4/competitions/"


response2=requests.get(url)
response2.status_code
source=response2.json()
print(source)


def all_name(source):
    """
    A function to extract all the names in the competition

    forloops: this is to iterate through the data and extract the names

    asigning the extracted names to name_of_comp

    Prints the extracted competition names.

    """
    for items in source['competitions']:
        name_of_comp=items['name']
        print(name_of_comp)
   
all_name(source)           