import boto3

s3 = boto3.client('s3')

#with open("text.py", 'rb') as f:
#     s3.put_object(Bucket="my-new-bucket-name-2024", Key="text.py", Body=f, ContentType="text/plain")

s3.upload_file('text.py', "my-new-bucket-name-2024", "test_upload.py", ExtraArgs={'ContentType':'text/plain'})

print('hi)')