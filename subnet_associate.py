import boto3

route_table_id = 'rtb-0eeaa2c7b25593d41'
subnet_id = 'subnet-09951d0e651112065'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])
