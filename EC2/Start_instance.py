import boto3

#Initialize Boto3 Clients fore Ec2
client = boto3.client('ec2')
response = client.start_instances(
    InstanceIds=['i-03bec857825337c5b']
    
)