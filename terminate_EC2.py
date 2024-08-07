import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify instance ID to start
instance_id = 'i-0dec7ea677be5e62a'

# Terminate the EC2 instance
response = ec2.terminate_instances(InstanceIds=[instance_id])

# Print response
print(response)