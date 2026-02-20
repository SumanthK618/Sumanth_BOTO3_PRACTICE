'''
Associated Route table to public Subnets
Link: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_route_table.html
'''

import boto3
client=boto3.client('ec2')

response= client.associate_route_table(
    
RouteTableId='rtb-0affdb2b5ca2c343a',
# SubnetId='subnet-0b3c6b171f5307e68',// can not perform 2 subnets at a time so i runned subnet-1 and commented it,so that i can run subnet-2.
SubnetId='subnet-0cede06b4d8de5d81'

)
                    