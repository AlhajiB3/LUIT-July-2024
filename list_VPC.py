import boto3

def describe_vpcs(client):
    response = client.describe_vpcs()
    
    for vpc in response["Vpcs"]:
        print(f"VPC ID: {vpc['VpcId']}, CIDR Block: {vpc['CidrBlock']}, Is Default: {vpc['IsDefault']}")
        
        # Check if VPC has tags
        if "Tags" in vpc:
            for tag in vpc["Tags"]:
                if tag["Key"] == "Name":
                    print(f"Name Tag: {tag['Value']}")
    
def describe_vpcs_with_filters(client, filters):
    response = client.describe_vpcs(Filters=filters)
    
    for vpc in response["Vpcs"]:
        print(f"VPC ID: {vpc['VpcId']}, CIDR Block: {vpc['CidrBlock']}, Is Default: {vpc['IsDefault']}")
        
        # Check if VPC has tags
        if "Tags" in vpc:
            for tag in vpc["Tags"]:
                if tag["Key"] == "Name":
                    print(f"Name Tag: {tag['Value']}")

if __name__ == "__main__":
    ec2 = boto3.client('ec2')
    
    # Describe all VPCs
    describe_vpcs(ec2)
    
    # Filters to get only default VPCs
    filters = [{'Name': 'isDefault', 'Values': ['true']}]
    describe_vpcs_with_filters(ec2, filters)

