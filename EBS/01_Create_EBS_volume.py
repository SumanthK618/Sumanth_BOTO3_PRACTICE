'''To Create EBS Volume
Link: https://docs.aws.amazon.com/boto3/latest/reference/services/ec2/client/create_volume.html
'''
import boto3
client=boto3.client('ec2')

response=client.create_volume(

      AvailabilityZone='ap-south-1a',
    Size=50,
    VolumeType='gp3', 
    
    
)