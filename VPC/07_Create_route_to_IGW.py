'''
Create Route
link: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_route.html
'''

import boto3
client=boto3.client('ec2')

response=client.create_route( 
   RouteTableId= 'rtb-0affdb2b5ca2c343a',
   DestinationCidrBlock='0.0.0.0/0',
   GatewayId='igw-0da2dfff8a57fd232'
)
          
          
          
          
          