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

    completed_tasks = [todo.get('title') for todo in todos_endpt
                       if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_endpt.get('name'), len(completed_tasks),
        len(todos_endpt)))
    [print("\t {}".format(comp)) for comp in completed_tasks]
