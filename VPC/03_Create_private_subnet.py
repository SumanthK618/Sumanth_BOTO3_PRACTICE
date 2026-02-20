'''
Created one subnet for private so this subnet we are attaching any gateways....
link:https://docs.aws.amazon.com/boto3/latest/reference/services/ec2/client/create_subnet.html#
'''

import boto3
client=boto3.client('ec2')

response=client.create_subnet(
    VpcId='vpc-095dc3ba4c6200126',
    CidrBlock='10.0.2.0/24'
    
    
)