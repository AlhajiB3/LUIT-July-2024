import boto3

def empty_bucket(client, bucket):
    # Initial listing of objects in the bucket
    response = client.list_objects_v2(Bucket=bucket)
    
    while "Contents" in response:
        # Create a list of objects to delete
        objects = [{'Key': content["Key"]} for content in response["Contents"]]
    
        # Delete the listed objects
        delete_response = client.delete_objects(
            Bucket=bucket,
            Delete={
                'Objects': objects
            }
        )
        
        # Check if there are more objects to delete
        if response.get("NextContinuationToken"):
            response = client.list_objects_v2(Bucket=bucket, 
                                              ContinuationToken=response["NextContinuationToken"])
        else:
            break

if __name__ == '__main__':
    # Initialize the S3 client
    s3 = boto3.client('s3')

    # Specify the bucket name
    bucket = "my-new-bucket-name-2024"

    # Empty the bucket
    empty_bucket(s3, bucket)

    # Delete the bucket
    response = s3.delete_bucket(Bucket=bucket)
    print(f"Bucket {bucket} deleted successfully")

