import boto3

internet_gateway_id = "igw-027598e082ee5b000"

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)
