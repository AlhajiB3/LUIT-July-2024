import boto3

def list_object_keys(client, bucket, prefix=''):
    keys = []
    kwargs = {'Bucket': bucket, 'Prefix': prefix}

    while True:
        resp = client.list_objects_v2(**kwargs)
        keys.extend([obj['Key'] for obj in resp.get('Contents', [])])
        
        if resp.get('IsTruncated'):  # More keys to retrieve
            kwargs['ContinuationToken'] = resp['NextContinuationToken']
        else:
            break

    return keys

def delete_object(client, bucket, key):
    response = client.delete_object(
        Bucket=bucket,
        Key=key
    )  
    
    return response
    
def delete_objects(client, bucket, keys):
    objects = [{'Key': key} for key in keys]
    print(f"Deleting objects: {objects}")  # Debug output

    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )
    
    return response

def delete_objects_non_recursive(client, bucket, keys, prefix):
    # Filter keys to remove those containing '/' after the prefix
    keys = [key for key in keys if '/' not in key[len(prefix):]]
    objects = [{'Key': key} for key in keys]
    print(f"Deleting non-recursive objects: {objects}")  # Debug output
    
    if not objects:
        print("No objects to delete.")
        return

    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )
    
    return response
    

if __name__ == '__main__':
    bucket = "my-new-bucket-name-2024"
    s3 = boto3.client('s3')
    
    prefix = "folder_txt_folder/"
    
    keys = list_object_keys(s3, bucket, prefix=prefix)
    print(f"Keys retrieved: {keys}")  # Debug output
    
    delete_objects_non_recursive(s3, bucket, keys, prefix)

