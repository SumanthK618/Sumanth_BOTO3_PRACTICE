'''
To Delete EBS Volume
Link: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_volume.html
'''


import boto3
client=boto3.client('ec2')

response=client.delete_volume(
    VolumeId='vol-0d1a30e7c94358cb7'
)