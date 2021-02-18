from addTodo import addTodoItem
from __future__ import print_function
import os
import boto3
import logging
from botocore.exceptions import ClientError
dynamodb = boto3.resource('dynamodb')

def handler(event,context):

    field = event['info']['fieldName']
    # todoId = event['arguments']['todoId']
    todo = event['arguments']['todo']


    if field == "addTodo":
        return addTodoItem(todo)
      
         