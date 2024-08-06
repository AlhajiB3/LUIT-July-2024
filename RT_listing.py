import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Describe all route tables
response = ec2.describe_route_tables()

# Iterate over each route table in the response
for route_table in response["RouteTables"]:
    print("VPC ID: {}, Route Table ID: {}".format(route_table['VpcId'], route_table['RouteTableId']))

    # Iterate over associations in the route table
    for association in route_table.get('Associations', []):
        print("Association ID: {}".format(association['RouteTableAssociationId']))
        if "SubnetId" in association:
            print("Subnet ID: {}".format(association['SubnetId']))
        else:
            print("No Subnet ID associated.")

    # Iterate over routes in the route table
    for route in route_table.get("Routes", []):
        print("Destination CIDR Block: {}, Gateway ID: {}".format(route['DestinationCidrBlock'], route.get('GatewayId', 'N/A')))

