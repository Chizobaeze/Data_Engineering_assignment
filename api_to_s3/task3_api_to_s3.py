import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()


baseurl = "https://randomuser.me/api/?results=500"

response_3 = requests.get(baseurl)

response_3.status_code()

data = response_3.json()


profile_of_male = []
profile_of_female = []
date_of_birth = []
full_name = []

for item in data['results']:
    if item['name']:
        first_name = item['name']['first']
        last_name = item['name']['last']
        full_name.append(f'my fulname is {first_name} {last_name}')

fullname = pd.DataFrame({'full_name': full_name})

session = boto3.Session(
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
