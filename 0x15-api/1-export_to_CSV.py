#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress,
records all tasks that are owned by this employee."""
if __name__ == "__main__":
    import csv
    import requests
    import sys

    fake_api = 'https://jsonplaceholder.typicode.com/'
    _id = sys.argv[1]
    employee = requests.get(fake_api + "users/{}".format(_id)).json()
    tasks = requests.get(fake_api + "todos", params={"userId": _id}).json()
    employee_username = user.get("username")
    with open("{}.csv".format(_id), "w", newline="") as csv_file:
    csv_w = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    [csv_w.writerow([_id, employee_username, task.get("completed"),
                     task.get("title")]) for task in tasks]
