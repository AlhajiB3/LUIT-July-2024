import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify instance ID and name for new AMI
instance_id = 'i-0dec7ea677be5e62a'
ami_name = 'my-ami3'
Image_Ids = 'ami-0a7347fd1793b97f0'
Owners = '590183779739'

# Create AMI
# response = ec2.create_image(InstanceId=instance_id, Name=ami_name)

# List AMIs 
# response = ec2.describe_images(ImageIds=Image_Ids, Owners=Owners)
response = ec2.describe_images

# Print AMI ID
print(response['ImageId'])

# Print Line Break
print("Line break")

# Print Describe Images
print(response['ImageId'], ['Owners'])