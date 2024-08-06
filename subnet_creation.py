import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Define the VPC ID and CIDR block for the subnet
vpc_id = 'vpc-07f2b356093629517'
cidr_block = '12.0.1.0/24'

# Create a subnet in the specified VPC
try:
    subnet_response = ec2.create_subnet(
        CidrBlock=cidr_block,
        VpcId=vpc_id
    )

    # Get the Subnet ID of the newly created subnet
    subnet_id = subnet_response['Subnet']['SubnetId']
    print("Created Subnet with ID:", subnet_id)

    # Optional: Tag the Subnet
    ec2.create_tags(
        Resources=[subnet_id],
        Tags=[{'Key': 'Name', 'Value': 'MyNewSubnet'}]
    )

    print("Subnet is now available and tagged.")
except boto3.exceptions.Boto3Error as e:
    print(f"An error occurred: {e}")

