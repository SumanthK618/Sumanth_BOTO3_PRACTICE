import boto3

client = boto3.client('s3',region_name='ap-south-1')

response = client.create_bucket(
    ACL='private',
    Bucket='boto3-bucket-feb-20-2026',
    
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)
print("s3 bucket created succesfully go and check in your s3 bucket")