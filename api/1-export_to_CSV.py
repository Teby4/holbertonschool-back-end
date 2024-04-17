#!/usr/bin/python3
"""task 1"""

import csv
import requests


def exportdata(argv):
    """export empleoyee data"""
    employee_id = argv[1]
    userlink = "https://jsonplaceholder.typicode.com/users/"
    user_response = requests.get("{}{}".format(userlink, employee_id))
    user = user_response.json()
    todolink = "https://jsonplaceholder.typicode.com/todos?userId="
    todo_response = requests.get("{}{}".format(todolink, employee_id))
    todos = todo_response.json()

    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([user['id'], user['name'],
                             todo['completed'], todo['title']])


if __name__ == "__main__":
    import sys
    exportdata(sys.argv)
