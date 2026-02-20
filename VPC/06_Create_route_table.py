'''
Create Route Table
Link: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_route_table.html
'''

import boto3
client=boto3.client('ec2')

response=client.create_route_table(
    VpcId='vpc-095dc3ba4c6200126'
)
