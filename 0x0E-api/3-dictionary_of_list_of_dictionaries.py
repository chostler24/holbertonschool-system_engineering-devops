#!/usr/bin/python3
"""
module
"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    user_response = requests.get(url)
    user_info = json.loads(user_response.text)
    tasks = {}
    for user in user_info:
        user_id = user['id']
        url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
            .format(user_id)
        todo_response = requests.get(url)
        todo_info = json.loads(todo_response.text)

        tasks_list = []
        for task in todo_info:
            task_dict = {}
            task_dict['username'] = user['username']
            task_dict['task'] = task['title']
            task_dict['completed'] = task['completed']
            tasks_list.append(task_dict)

        tasks[user_id] = tasks_list
    with open('todo_all_employees.json', 'w', encoding='UTF8',
              newline='') as f:
        f.write(json.dumps(tasks))
