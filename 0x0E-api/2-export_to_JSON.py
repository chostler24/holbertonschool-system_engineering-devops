#!/usr/bin/python3
"""module"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = requests.get(url)
    url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
        .format(user_id)
    todo_response = requests.get(url)
    user_info = json.loads(user_response.text)
    todo_info = json.loads(todo_response.text)
    tasks = {}
    tasks_list = []

    for task in todo_info:
        task_dict = {}
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']
        task_dict['username'] = user_info['username']
        tasks_list.append(task_dict)

    tasks[user_id] = tasks_list

    with open('./{}.json'.format(user_id), 'w', encoding='UTF8',
              newline='') as f:
        f.write(json.dumps(tasks))
