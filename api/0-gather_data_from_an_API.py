#!/usr/bin/python3
"""0-gather_data_from_an_API task"""


import sys
import requests


def get_employee(argv):
    """Get employee data and print completed tasks.

    Args:
        argv (list): List of command-line arguments, where the first argument is
                     the employee ID.
    """
    empleoyeid = argv[1]
    userlink = "https://jsonplaceholder.typicode.com/users/"
    user_response = requests.get("{}{}".format(userlink, empleoyeid))
    user = user_response.json()
    todolink = "https://jsonplaceholder.typicode.com/todos?userId="
    todo_response = requests.get("{}{}".format(todolink, empleoyeid))
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
