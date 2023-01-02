import boto3

def lambda_handler(event, context):
    # Get list of regions
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_regions()
    regions = [region['RegionName'] for region in response['Regions']]

    # Iterate over each region
    for region in regions:
        # Stop the running instances in the region
        ec2_client = boto3.client('ec2', region_name=region)
        instances = [instance.id for instance in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])]
        if instances:
            ec2_client.stop_instances(InstanceIds=instances)
            print("Stopped instances:", instances)
        else:
            print("No running instances found in region:", region)
