''' To Create IAM User
Link: https://docs.aws.amazon.com/boto3/latest/reference/services/iam/client/create_user.html#
'''
import boto3

client=boto3.client('iam')

response= client.create_user(
    UserName='sumanth-user',
    Path='/'
)
    
    

