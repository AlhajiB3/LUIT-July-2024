import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# List security groups
response = ec2.describe_security_groups()

# Print security group details
for sg in response['SecurityGroups']:
    print(f"Security Group ID: {sg['GroupId']}, Name: {sg['GroupName']}, Description: {sg['Description']}")

# Optional: Print entire response for reference
# print(response)
