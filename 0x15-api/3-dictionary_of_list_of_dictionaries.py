#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests


def get_user_todos(user_id, base_url):
    """Fetch the to-do list for a specific user."""
    todos_response = requests.get(
        base_url + "todos", params={"userId": user_id})
    return todos_response.json()


def create_user_tasks_mapping(users, base_url):
    """
    Create a dictionary mapping user IDs to their tasks in JSON format.

    Parameters:
        users (list): A list of dictionaries containing user information.
        base_url (str): The base URL for the API.

    Returns:
        dict: A dictionary mapping user IDs to their tasks.
    """
    user_tasks = {}
    for user in users:
        user_id = user.get("id")
        todos = get_user_todos(user_id, base_url)
        user_tasks[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            }
            for todo in todos
        ]
    return user_tasks


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users_response = requests.get(base_url + "users")
    users = users_response.json()

    user_tasks = create_user_tasks_mapping(users, base_url)

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(user_tasks, jsonfile)
