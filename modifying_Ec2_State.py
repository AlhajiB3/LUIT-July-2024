import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify instance ID to stop
instance_id = 'i-0c4fe66e6df83cc6b'

# Stop the EC2 instance
response = ec2.stop_instances(InstanceIds=[instance_id])

# Print response
print(response)