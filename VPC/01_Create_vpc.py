'''
created a VPC
link:https://docs.aws.amazon.com/boto3/latest/reference/services/ec2/client/create_vpc.html#
'''

import boto3

client=boto3.client('ec2')

response = client.create_vpc(
    CidrBlock='10.0.0.0/16'
)