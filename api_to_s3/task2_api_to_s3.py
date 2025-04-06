import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

url = "http://api.football-data.org/v4/competitions/"
response2 = requests.get(url)
response2.status_code
source = response2.json()

competition_name = []
for items in source['competitions']:
    name_of_comp = items['name']
    competition_name.append(name_of_comp)

competition_name = pd.DataFrame({'names': competition_name})

load_dotenv()

session = boto3.Session(
        aws_access_key_id=os.getenv('aws_access_key'),
        aws_secret_access_key=os.getenv('aws_secret_key'),
        region_name="eu-central-1"
)

wr.s3.to_parquet(
    df=competition_name,
    path="s3://chizoba-loaded-api/task2-name-of-comp/",
    boto3_session=session,
    mode="append",
    dataset=True
   )
