import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Define the subnet ID
subnet_id = "subnet-09951d0e651112065"

try:
    # Check if the subnet is associated with any route table
    route_tables = ec2.describe_route_tables()
    for rt in route_tables['RouteTables']:
        for association in rt['Associations']:
            if 'SubnetId' in association and association['SubnetId'] == subnet_id:
                ec2.disassociate_route_table(AssociationId=association['RouteTableAssociationId'])
                print(f"Disassociated subnet {subnet_id} from route table {rt['RouteTableId']}")
    
    # Delete the subnet
    ec2.delete_subnet(SubnetId=subnet_id)
    print(f"Subnet {subnet_id} deleted successfully")
except (BotoCoreError, ClientError) as error:
    print(f"An error occurred: {error}")

