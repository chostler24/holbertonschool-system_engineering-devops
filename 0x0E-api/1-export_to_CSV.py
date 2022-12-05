#!/usr/bin/python3
"""module"""
import json
import requests
from sys import argv
import csv


if __name__ == "__main__":
    num_done, num_tasks = 0, 0
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = requests.get(url)
    url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
        .format(user_id)
    todo_response = requests.get(url)
    user_info = json.loads(user_response.text)
    todo_info = json.loads(todo_response.text)

    task_list = []
    username = user_info['username']
    for task in todo_info:
        task_dict = {}
        task_dict['USER_ID'] = user_id
        task_dict['USERNAME'] = username
        task_dict['TASK_COMPLETED_STATUS'] = task['completed']
        task_dict['TASK_TITLE'] = task['title']
        task_list.append(task_dict)

    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    with open('./{}.csv'.format(user_id), 'w', encoding='UTF8',
              newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL, quotechar='"')
        writer.writerows(task_list)
