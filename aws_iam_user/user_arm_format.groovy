Document source for s3:
https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html

S3 accesspoint:
arn:${Partition}:s3:${Region}:${Account}:accesspoint/${AccessPointName}


S3 bucket:
arn:${Partition}:s3:::${BucketName}


S3 storagelensgroup:
arn:${Partition}:s3:${Region}:${Account}:storage-lens-group/${Name}


S3 object:
arn:${Partition}:s3:::${BucketName}/${ObjectName}

Document source for IAM:
https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html

IAM mfa:
arn:${Partition}:iam::${Account}:mfa/${MfaTokenIdWithPath}


IAM role:
arn:${Partition}:iam::${Account}:role/${RoleNameWithPath}


IAM user:
arn:${Partition}:iam::${Account}:user/${UserNameWithPath}


Document source for ec2:
https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html
EC2 elastic-ip:
arn:${Partition}:ec2:${Region}:${Account}:elastic-ip/${AllocationId}



EC2 fleet:
arn:${Partition}:ec2:${Region}:${Account}:fleet/${FleetId}


EC2 instance:
arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}


EC2  image:
arn:${Partition}:ec2:${Region}::image/${ImageId}


