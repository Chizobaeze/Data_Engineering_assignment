import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://content.guardianapis.com/search?api-key=test&q=Nigeria&page-" \
       "size=100&from-date=2025-01-01"

response = requests.get(url)
response.status_code


data = response.json()

result = data['response']['results']

codeurl = []


for url in result:
    if "webUrl" in url:
        codeurl.append(url["webUrl"])
df = pd.DataFrame({'Url': codeurl})


session = boto3.Session(
        aws_access_key_id=os.getenv('aws_access_key'),
        aws_secret_access_key=os.getenv('aws_secret_key'),
        region_name="eu-central-1"
)

wr.s3.to_parquet(
    df=df,
    path="s3://chizoba-loaded-api/task4-guardian-api/",
    boto3_session=session,
    mode="append",
    dataset=True
)
