import boto3
import os
import logging
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
tableName = os.environ['TODOS_TABLE']


async def addTodoItem(todo):
    try:
        res = tableName.put_item(
            Item={todo}
        )
    except ClientError as e:
        logging.error(e) 
    return res
