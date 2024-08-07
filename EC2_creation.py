import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def launch_ec2_instance():
    try:
        # Create EC2 client
        ec2 = boto3.client('ec2')

        # Specify AMI, instance type, key pair, security group, and subnet
        ami_id = 'ami-0a7347fd1793b97f0'
        instance_type = 't2.micro'
        key_name = 'my-key-pair'
        security_group_ids = ['sg-00621162195638ce7']
        subnet_id = 'subnet-0f4e7f06e263fe077'  # Replace with your subnet ID

        # Launch new EC2 instance
        response = ec2.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            KeyName=key_name,
            MaxCount=1,  # Required parameter
            MinCount=1,  # Required parameter
            SecurityGroupIds=security_group_ids,
            SubnetId=subnet_id
        )

        # Print instance ID
        instance_id = response['Instances'][0]['InstanceId']
        print(f'Launched instance {instance_id}')

    except NoCredentialsError:
        print("Error: No AWS credentials found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials found.")
    except ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    launch_ec2_instance()
