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
    userID = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userID)).json()
    tod = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                       .format(userID)).json()
    completed_tasks = []
    for task in tod:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
        print("Employee {} is done with tasks({}/{}):".
                  format(user.get('name'), len(completed_tasks), len(tod)))
        print("\n".join("\t {}".format(task) for task in completed_tasks))
