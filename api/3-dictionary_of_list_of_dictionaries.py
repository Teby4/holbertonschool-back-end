#!/usr/bin/python3
"""3-dictionary_of_list_of_dictionaries"""

import json
import requests
import sys


def dictlist(argv):
    """get all employees data"""
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)
    users = users_response.json()
    todos = todos_response.json()

    all_users_tasks = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_tasks = []

        for task in todos:
            if task.get('userId') == user_id:
                task_info = {
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                user_tasks.append(task_info)

        all_users_tasks[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_users_tasks, json_file)


if __name__ == "__main__":
    dictlist(sys.argv)
