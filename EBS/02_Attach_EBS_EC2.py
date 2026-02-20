'''
To Attach EBS Volume
Link:https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/attach_volume.html
'''


import boto3
client=boto3.client('ec2')

response = client.attach_volume(
    VolumeId='vol-0d1a30e7c94358cb7',   
    InstanceId='i-03bec857825337c5b',   
    Device='/dev/sdf'    
    )