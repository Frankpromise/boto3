import boto3
from datetime import datetime, timedelta
def lambda_handler(event, context):
    # Set the maximum age (in days) of the AMIs that you want to deregister
    max_age = 30

    # Get the current timestamp and compute the cutoff timestamp
    now = datetime.utcnow()
    cutoff = now - timedelta(days=max_age)

    # Iterate over the regions
    for region in boto3.client('ec2').describe_regions()['Regions']:
        # Connect to the EC2 service in the region
        ec2 = boto3.client('ec2', region_name=region['RegionName'])

        # Get a list of all AMIs in the region
        amis = ec2.describe_images(Owners=['self'])['Images']

        # Iterate over the AMIs
        for ami in amis:
            # Get the creation date of the AMI
            creation_date = ami['CreationDate']

            # Convert the creation date to a datetime object
            creation_timestamp = datetime.strptime(creation_date, '%Y-%m-%dT%H:%M:%S.%fZ')

            # If the AMI is older than the maximum age, deregister it
            if creation_timestamp < cutoff:
                print(f'Deregistering AMI {ami["ImageId"]} in {region["RegionName"]}')
                ec2.deregister_image(ImageId=ami['ImageId'])
