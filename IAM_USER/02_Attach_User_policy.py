'''
To attach Iam User policy(AWS Managed Policy)
Link: Attach Managed Policy
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/attach_user_policy.html
'''
import boto3
client=boto3.client('iam')

resource=client.attach_user_policy(
    UserName='sumanth-user',
    PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
    
)
resource=client.attach_user_policy(
    UserName='sumanth-user',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'
    
)