#!/usr/bin/python3
"""
This script retrieves to-do list information for a given employee ID
using the JSONPlaceholder API.
"""

import requests
import sys


def get_employee_todos(employee_id):
    """
    Get the to-do list information for a given employee ID.

    Parameters:
        employee_id (int): The ID of the employee whose to-do list
        is to be fetched.

    Returns:
        tuple: A tuple containing the employees name, number of completed tasks
        and the list of completed tasks.
    """
    base_url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(base_url + "users/{}".format(employee_id))
    user = user_response.json()

    todos_response = requests.get(
        base_url + "todos", params={"userId": employee_id})
    todos = todos_response.json()

    completed_tasks = [todo.get("title")
                       for todo in todos if todo.get("completed")]

    return user.get("name"), len(completed_tasks), completed_tasks


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        name, num_completed_tasks, completed_tasks = get_employee_todos(
            employee_id)

        print("Employee {} is done with tasks({}/{}):".format(name,
              num_completed_tasks, len(completed_tasks)))
        for task in completed_tasks:
            print("\t", task)

    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    except requests.exceptions.RequestException as e:
        print("Error: Failed to fetch data from the API.")
        sys.exit(1)
