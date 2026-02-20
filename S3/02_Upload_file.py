import boto3

client=boto3.client('s3',region_name='ap-south-1')        ## i didnot specify default region in aws CLI while configuring in terminal aws configure,
                                                          ##so i am specifying region name here.
                                                    
client.upload_file('To_upload_in_s3_img.png','boto3-bucket-feb-20-2026','NLB_image.png')

                 #('file name/path of file  ,    's3-bucket-name'      ,  'object_name')
                 
                 
                    
# aws s3 ls --> shows list of buckets
#aws s3 ls s3://boto3-bucket-feb-20-2026 --> shows objects inside the bucket
          
                 
                 
                 
