import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def create_instance(client, ami_id, security_group_id, key_pair_name, subnet_id, user_data=None):
    try:
        response = client.run_instances(
            ImageId=ami_id,
            InstanceType='t2.micro',
            KeyName=key_pair_name,
            MaxCount=1,
            MinCount=1,
            SecurityGroupIds=[
                security_group_id
            ],
            SubnetId=subnet_id,
            UserData=user_data
        )
        
        instance_id = response["Instances"][0]["InstanceId"]
        print(f'Launched instance {instance_id}')
    
    except NoCredentialsError:
        print("Error: No AWS credentials found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials found.")
    except ClientError as e:
        print(f"Error: {e}")

ami_id = "ami-0a7347fd1793b97f0"
key_pair_name = "my-key-pair"
security_group_id = "sg-09542c8bfa65a9c27"
subnet_id = "subnet-0f4e7f06e263fe077"  # Your existing subnet ID

user_data='''#!/bin/bash
apt update -y
apt-get install -y apache2
systemctl start apache2
systemctl enable apache2'''

ec2 = boto3.client('ec2')
create_instance(ec2, ami_id, security_group_id, key_pair_name, subnet_id, user_data)

