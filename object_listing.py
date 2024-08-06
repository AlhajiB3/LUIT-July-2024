import boto3

def filter_objects_extension(client, bucket, extension):
    key = []
    response = client.list_objects_v2(Bucket=bucket)
    for content in response["Contents"]:
        if(extension in content["Key"][-(len(extension)):]):
           keys.append(content["Key"])

           return keys

     

s3 = boto3.client('s3')

response = def filter_objects_extension(s3, "my-new-bucket-name-2024", ".txt")


