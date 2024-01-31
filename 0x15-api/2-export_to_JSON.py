#!/usr/bin/python3
"""
export all tasks that are owned by this employee in the JSON format.
"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    fake_api = 'https://jsonplaceholder.typicode.com/'
    _id = sys.argv[1]
    employee = requests.get(fake_api + "users/{}".format(_id)).json()
    tasks = requests.get(fake_api + "todos", params={"userId": _id}).json()
    employee_username = user.get("username")

    with open("{}.json".format(_id), "w") as jsonfile:
        json.dump({_id: [{"task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_username
            } for task in tasks]}, jsonfile)
