#!/usr/bin/python3
"""module"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    ID = argv[1]
    API_URL = 'https://jsonplaceholder.typicode.com/'
    url = API_URL + 'users/{}'.format(ID)
    user_response = requests.get(url)
    profile = json.loads(user_response.text)
    name = profile['name']
    url_list = API_URL + 'todos/?userId={}'.format(ID)
    todos_repsonse = requests.get(url_list)
    todos_list = todos_repsonse.text
    tasks = json.loads(todos_list)
    tasks_done = []
    tasks_done_count = 0

    for task in tasks:
        if task.get('completed'):
            tasks_done.append(task)
            tasks_done_count += 1

    first_prompt = "Employee {} is done with ".format(name)
    sec_prompt = "tasks({}/{}):".format(tasks_done_count, len(tasks))
    print(first_prompt + sec_prompt)
    for todo in tasks_done:
        print("\t {}".format(todo.get('title')))
