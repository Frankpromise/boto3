import boto3
import pprint
from boto3.dynamodb.conditions import Key, Attr

# use the created table
import boto3
session = boto3.Session(region_name="us-west-2")
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('users')
print(table.creation_date_time)


#Add item to table

table.put_item(
   Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'Last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)


# get an item

response = table.get_item(
    Key={
        'username': 'janedoe',
        'Last_name': 'Doe'
    }
)
item = response['Item']
print(item)


# # update table

table.update_item(
    Key={
        'username': 'janedoe',
        'Last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)

item = response['Item']

pprint.pprint(item)

# delete an item

table.delete_item(
    Key={
        'username': 'janedoe',
        'Last_name': 'Doe'
    }
)

# This queries for all of the users whose username key equals janedoe

response = table.query(
    KeyConditionExpression=Key('username').eq('janedoe')
)
items = response['Items']
pprint.pprint(items)