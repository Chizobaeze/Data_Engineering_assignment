import os
import pandas as pd
from job_icy import response
import boto3
import awswrangler as wr
from dotenv import load_dotenv
load_dotenv()

roles = response['jobs']


actual_job = []
manager_job = []
for role in roles:

    """
    Iterates through a list of roles.
    Checks if the job title contains the word 'Senior'.
    if it has senior in it then, print actual _job.
    if it doesnt then, it is added to the manager_job.

    """
    if 'Senior' in role['jobTitle']:
        actual_job.append(role['jobTitle'])
    if 'Manager' in role['jobTitle']:
        manager_job.append(role['jobTitle'])

senior = pd.DataFrame({'senior_role': actual_job})
manager = pd.DataFrame({'manager_role': manager_job})

session = boto3.Session(
          aws_access_key_id=os.getenv('aws_access_key'),
          aws_secret_access_key=os.getenv('aws_secret_key'),
          region_name="eu-central-1"
)

wr.s3.to_parquet(
    df=senior,
    path="s3://chizoba-loaded-api/task1-jobtitle/",
    boto3_session=session,
    mode="append",
    dataset=True
)

wr.s3.to_parquet(
    df=manager,
    path="s3://chizoba-loaded-api/task1-jobtitle/",
    boto3_session=session,
    mode="append",
    dataset=True
)
