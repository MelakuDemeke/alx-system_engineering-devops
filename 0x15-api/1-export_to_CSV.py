#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""

import csv
import requests
import sys


def export_todo_list_to_csv(user_id):
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

    # Write to CSV file
    csv_filename = "{}.csv".format(user_id)
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            csv_writer.writerow(
                [user_id, username, todo.get("completed"), todo.get("title")])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_todo_list_to_csv(user_id)
