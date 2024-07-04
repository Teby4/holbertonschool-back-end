#!/usr/bin/python3
"""0-gather_data_from_an_API task"""


import sys
import requests
import json

def dictlist(argv):
    """get empleoye data"""
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)
    users = users_response.json()
    todos = todos_response.json()

    all_users_tasks = {}
    
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = []
        
        for task in todos:
            if task['userId'] == user_id:
                task_info = {
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                user_tasks.append(task_info)
        
        all_users_tasks[user_id] = user_tasks
    
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_users_tasks, json_file)

if __name__ == "__main__":
    dictlist(sys.argv)