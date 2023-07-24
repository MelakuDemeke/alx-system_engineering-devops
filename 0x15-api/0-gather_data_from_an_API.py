#!/usr/bin/python3
"""
Employee To-Do List

This script fetches and displays the to-do list information for
a given employee ID.It uses the JSONPlaceholder API
(https://jsonplaceholder.typicode.com/)

Usage:
    python script_name.py employee_id

Arguments:
    employee_id (int): The ID of the employee whose to-do list you want to view

Example:
    python script_name.py 3
"""

import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(base_url + "todos", params={"userId": sys.argv[1]}).json()

    completed_tasks = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))
    [print("\t {}".format(c)) for c in completed_tasks]
