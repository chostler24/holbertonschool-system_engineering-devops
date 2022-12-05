#!/usr/bin/python3
"""module"""
import json
import requests
from sys import argv
import csv


if __name__ == "__main__":
    USER_ID = argv[1]
    API_URL = 'https://jsonplaceholder.typicode.com/'
    url = API_URL + 'users/{}'.format(USER_ID)
    user_response = requests.get(url)
    profile = json.loads(user_response.text)
    name = profile['name']
    url_list = API_URL + 'todos/?userId={}'.format(USER_ID)
    todos_repsonse = requests.get(url_list)
    todos_list = todos_repsonse.text
    tasks = json.loads(todos_list)
    tasks_done = []
    tasks_done_count = 0

    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    with open('./{}.csv'.format(USER_ID), 'w', encoding='UTF-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL, quotechar='"')
        writer.writerows(tasks_done)
