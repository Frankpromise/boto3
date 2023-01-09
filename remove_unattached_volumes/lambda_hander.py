import boto3

def delete_unattached_volumes():
    # Get list of all regions
    ec2 = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]
    
    # Iterate over all regions
    for region in regions:
        print(f"Checking region {region}")
        ec2 = boto3.client('ec2', region_name=region)
        
        # Get list of all unattached volumes in the region
        volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])['Volumes']
        
        # Iterate over the volumes and delete them
        for volume in volumes:
            volume_id = volume['VolumeId']
            print(f"Deleting volume {volume_id}")
            ec2.delete_volume(VolumeId=volume_id)

def lambda_handler(event, context):
    delete_unattached_volumes()
