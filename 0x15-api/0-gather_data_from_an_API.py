#!/usr/bin/python3
"""Script that uses given rest api to return info
about employee to do list"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user_endpt = requests.get(url + "users/{}".format(user_id)).json()
    todos_endpt = requests.get(url + "todos?userId={}".format(
                               user_id)).json()

    completed_tasks = [todo.get('title') for todo in todos
                       if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_endpt.get('name'), len(completed), len(todos)))
    [print("\t {}".format(c)) for comp in completed_tasks]
