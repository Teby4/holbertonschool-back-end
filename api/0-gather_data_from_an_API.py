#!/usr/bin/python3
"""0-gather_data_from_an_API task"""


import sys
import requests


def get_employee(argv):
    """get empleoye data"""
    empleoyeid = argv[1]
    user_link = "https://jsonplaceholder.typicode.com/users/"
    user_response = requests.get("{}{}".format(user_link, empleoyeid))
    user = user_response.json()
    todo_link = "https://jsonplaceholder.typicode.com/todos?userId="
    todo_response = requests.get("{}{}".format(todo_link, empleoyeid))
    todos = todo_response.json()

    task_completed = 0
    for todo in todos:
        if todo.get('completed'):
            task_completed += 1

    total_tasks = len(todos)
    print(f"Employee {user.get('name')} is done with tasks"
          f"({task_completed}/{total_tasks}):")

    for todo in todos:
        if todo.get('completed'):
            print(f"\t {todo.get('title')}")


if __name__ == "__main__":
    get_employee(sys.argv)
