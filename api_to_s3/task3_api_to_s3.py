import requests
import pandas  as pd

baseurl="https://randomuser.me/api/?results=500"

response_3=requests.get(baseurl)

data=response_3.json()


profile_of_male = []
profile_of_female= []
date_of_birth=[]
full_name=[]
    
    
for item in data['results']:
        
        """
        created an empty list for male and female gender,date_of_birth and full_name

        for loops to iterate through the result list 

        Extracts gender, birth date, and full name for each user
        """
    
        if item['gender']=='male':
            profile_of_male.append('male')
        elif item['gender']=='female':
            profile_of_female.append('female')
            
        if   item['dob']:
            birth_date = item['dob']['date']
            date_of_birth.append(birth_date)
        if item['name']:
            first_name= item['name']['first']
            last_name=item['name']['last']
            full_name.append(f'my fulname is {first_name} {last_name}')
            
            

full_name

fullname = pd.DataFrame({'full_name':full_name})


import os
import boto3
import awswrangler as wr
from dotenv import load_dotenv ,dotenv_values

filename="fullname"

load_dotenv()

session=boto3.Session(
 aws_access_key_id=os.getenv('aws_access_key'),
aws_secret_access_key=os.getenv('aws_secret_key'),
region_name="eu-central-1"    
)


wr.s3.to_parquet(
     df=fullname,
     path='s3://chizoba-loaded-api/task3-fullname/',
     boto3_session=session,
    mode="append",
    dataset=True 
)

