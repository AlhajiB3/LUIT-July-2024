import boto3

route_table_id = "rtb-0eeaa2c7b25593d41"
internet_gateway_id = "igw-027598e082ee5b000"

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)
