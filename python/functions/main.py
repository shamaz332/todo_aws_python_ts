from __future__ import print_function
from addTodo import addTodoItem
import os
import boto3
import logging
from botocore.exceptions import ClientError
dynamodb = boto3.resource('dynamodb')

def handler(event,context):
    print(event)
    field = event['info']['fieldName']
    # todoId = event['arguments']['todoId']
    todo = event['arguments']['todo']
    print(field)


    if field == "addTodo":
        addTodoItem(todo)
    # else:
    #     null