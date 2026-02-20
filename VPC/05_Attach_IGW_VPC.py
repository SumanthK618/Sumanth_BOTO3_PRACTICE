'''
Attach Internet Gateway to VPC
Link: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/attach_internet_gateway.html

'''
import boto3 

client=boto3.client('ec2')

response=client.attach_internet_gateway(
InternetGatewayId='igw-0da2dfff8a57fd232',
VpcId='vpc-095dc3ba4c6200126'
)