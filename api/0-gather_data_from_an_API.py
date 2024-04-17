#!/usr/bin/python3


import requests
import json

def get_employee(argv):
    empleoyeid = argv[1]
    user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(empleoyeid))
    user = user_response.json()
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(empleoyeid))
    todos = todo_response.json()

    task_completed = 0
    for todo in todos:
        if todo['completed']:
            task_completed += 1

    total_tasks = len(todos)
    print(f"Employee {user['name']} is done with tasks ({task_completed}/{total_tasks}):")

    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")

if __name__ == "__main__":
    import sys
    get_employee(sys.argv)
