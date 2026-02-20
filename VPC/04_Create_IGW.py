'''
Create Internet Gateway (IGW)
Link :https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_internet_gateway.html
'''

import boto3

client = boto3.client('ec2')

response=client.create_internet_gateway(
   
)