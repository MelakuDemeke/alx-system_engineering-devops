#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.
"""

import json
import requests
import sys


def export_todo_list_to_json(user_id):
    # API base URL
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user_response = requests.get(base_url + "users/{}".format(user_id))
    user = user_response.json()
    username = user.get("username")

    # Fetch to-do list for the user
    todos_response = requests.get(
        base_url + "todos", params={"userId": user_id})
    todos = todos_response.json()

    # Prepare JSON data
    json_data = {
        user_id: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        } for todo in todos]
    }

    # Write to JSON file
    json_filename = "{}.json".format(user_id)
    with open(json_filename, "w") as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_todo_list_to_json(user_id)
