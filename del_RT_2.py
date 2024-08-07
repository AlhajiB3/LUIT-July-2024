import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Define the route table ID
route_table_id = "rtb-0eeaa2c7b25593d41"

# Initialize the EC2 client
ec2 = boto3.client('ec2')

try:
    # Delete the route table
    ec2.delete_route_table(RouteTableId=route_table_id)
    print(f"Route table {route_table_id} deleted successfully")

except (BotoCoreError, ClientError) as error:
    print(f"An error occurred: {error}")
