#!/usr/bin/python3
"""Script that uses given rest api to return info
about employee to do list"""
import csv
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

    """Task 1 export to csv"""
    csv_file = "{}.csv".format(user_id)
    with open(csv_file, "w", newline="") as csvf:
        writer_obj = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        for todo in todos_endpt:
            writer_obj.writerow([user_id, user_endpt.get('name'),
                                 todo.get('completed'),
                                 todo.get('title')])
