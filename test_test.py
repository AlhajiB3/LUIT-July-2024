import boto3

# Initialize a session using Amazon S3
s3 = boto3.client('s3', region_name='us-east-1')

# Create a new bucket
try:
    response = s3.create_bucket(
        Bucket='my-new-bucket-name-2024'  # Replace with a valid name
    )
    print(f'Bucket {response["Location"]} created successfully.')
except Exception as e:
    print(f'Error: {e}')

