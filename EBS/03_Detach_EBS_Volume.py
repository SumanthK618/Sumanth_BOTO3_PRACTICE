'''To Detach EBS Volume
Link: https://docs.aws.amazon.com/boto3/latest/reference/services/ec2/client/detach_volume.html#
'''
import boto3
client=boto3.client('ec2')

response=client.detach_volume(
    Device='/dev/sdf',
    InstanceId='i-03bec857825337c5b',
    VolumeId='vol-0d1a30e7c94358cb7'
    
    
)