import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def create_vpc_and_subnet():
    try:
        # Create EC2 client
        ec2 = boto3.client('ec2')

        # Step 1: Create a VPC
        vpc_response = ec2.create_vpc(
            CidrBlock='10.0.0.0/16',
        )
        vpc_id = vpc_response['Vpc']['VpcId']
        print(f'Created VPC with ID: {vpc_id}')

        # Tag the VPC
        ec2.create_tags(
            Resources=[vpc_id],
            Tags=[{'Key': 'Name', 'Value': 'MyVPC'}]
        )

        # Step 2: Create a Subnet within the VPC
        subnet_response = ec2.create_subnet(
            VpcId=vpc_id,
            CidrBlock='10.0.1.0/24',
        )
        subnet_id = subnet_response['Subnet']['SubnetId']
        print(f'Created Subnet with ID: {subnet_id}')

        # Tag the Subnet
        ec2.create_tags(
            Resources=[subnet_id],
            Tags=[{'Key': 'Name', 'Value': 'MySubnet'}]
        )

        return vpc_id, subnet_id

    except NoCredentialsError:
        print("Error: No AWS credentials found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials found.")
    except ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_vpc_and_subnet()

