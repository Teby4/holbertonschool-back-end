#!/usr/bin/python3
"""task 1"""

import json
import requests


def exportdata(argv):
    """export empleoyee data"""
    employee_id = argv[1]
    user_link = "https://jsonplaceholder.typicode.com/users/"
    user_response = requests.get("{}{}".format(user_link, employee_id))
    user = user_response.json()
    todo_link = "https://jsonplaceholder.typicode.com/todos?userId="
    todo_response = requests.get("{}{}".format(todo_link, employee_id))
    todos = todo_response.json()

    filename = f"{employee_id}.json"

    tasks = []
    for todo in todos:
        task = {
            "task": todos.get('title'),
            "completed": todos.get('completed'),
            "username": user.get('username')
            }
        tasks.append(task)

    data = {
        employee_id: tasks
    }
    with open(filename, mode='w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    import sys
    exportdata(sys.argv)
