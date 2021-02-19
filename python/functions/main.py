from __future__ import print_function
from addTodo import addTodoItem
from getTodo import getItem
from deleteTodo import deleteItem
from updateTodo import updateItem
import os
import boto3
import logging
from botocore.exceptions import ClientError
dynamodb = boto3.resource('dynamodb')


def handler(event, context):

    field = event['info']['fieldName']



    if field == "addTodo":
        todo = event['arguments']['todo']
        addTodoItem(todo)
    elif field == "getTodos":
        getItem()
    elif field == "deleteTodo":
        todoId = event['arguments']['todoId']
        deleteItem(todoId)
    elif field == "updateTodo":
        todo = event['arguments']['todo']
        updateItem(todo)
    else:
        print("No matched")
