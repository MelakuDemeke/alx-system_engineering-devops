#!/usr/bin/python3
"""
Employee To-Do List

This script fetches and displays the to-do list information for
a given employee ID.It uses the JSONPlaceholder API
(https://jsonplaceholder.typicode.com/)

Usage:
    python script_name.py employee_id

Arguments:
    employee_id (int): The ID of the employee whose to-do list
    you want to view.

Example:
    python script_name.py 3
"""

import requests
import sys


def get_employee_todos(employee_id):
    """
    Retrieves the to-do list for the specified employee ID and
    displays completed tasks.

    Parameters:
        employee_id (int): The ID of the employee whose to-do list
        you want to view.
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + "users/{}".format(employee_id)).json()
    todos = requests.get(base_url + "todos",
                         params={"userId": employee_id}).json()

    completed_tasks = [todo.get("title")
                       for todo in todos if todo.get("completed")]
    total_tasks = len(todos)

    print("Employee {} has completed {}/{} tasks:".format(user.get("name"),
          len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todos(employee_id)
