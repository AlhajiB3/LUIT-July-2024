
import boto3

vpc_id = "vpc-07f2b356093629517"

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)
