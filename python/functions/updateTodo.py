from decimal import Decimal
from pprint import pprint
import boto3
import os
import logging
from botocore.exceptions import ClientError
import json
import re

dynamodb = boto3.resource('dynamodb')
tableName = os.environ['TODOS_TABLE']
table = dynamodb.Table(tableName)
print(tableName)


def updateItem(todo):

    try:
        res = table.update_item(
            Key={
                id: todo.id
            },
            ExpressionAttributeValues={
                ":d": todo.title
            },
            UpdateExpression="set title = :d",
            ReturnValues="Updated_New",



        )
    except ClientError as e:
        logging.error(e)
    return json.dumps(todo)

    # prefix = "set"
    # attributes = todo.keys()
    # for i in range(len(attributes)):
    #     attribute = attributes[i]
    #     if attribute != "id":
    #         params["UpdateExpression"] += prefix + \
    #             "#" + attribute + " = :" + attribute
    #         params["ExpressionAttributeValues"][":" +
    #                                             attribute] = todo[attribute]
    #         params["ExpressionAttributeNames"]["#" + attribute] = attribute
    #         prefix = ", "
    #         prefix = ", "
