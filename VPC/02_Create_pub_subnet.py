
'''created 2  subnets we will use this as public subnet after attaching to Internet gateway....
link:https://docs.aws.amazon.com/boto3/latest/reference/services/ec2/client/create_subnet.html#
'''

import boto3

client= boto3.client('ec2')

response1=client.create_subnet(
    
    VpcId='vpc-095dc3ba4c6200126',
    CidrBlock='10.0.0.0/24'
)
response2=client.create_subnet(
    VpcId='vpc-095dc3ba4c6200126',
    CidrBlock='10.0.1.0/24'
)
    
    
    

