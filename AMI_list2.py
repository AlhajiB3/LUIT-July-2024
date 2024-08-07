import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify the Owner ID (your AWS account ID)
Owners = ['590183779739']  # Replace with your AWS account ID

# List AMIs created by your AWS account
response = ec2.describe_images(Owners=Owners)

# Print AMI IDs and their names
for image in response['Images']:
    print(f"Image ID: {image['ImageId']}, Name: {image['Name']}")

# Print Describe Images response
print(response['Images'])
