import boto3

internet_gateway_id = "igw-027598e082ee5b000"
vpc_id = "vpc-07f2b356093629517"

ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)
