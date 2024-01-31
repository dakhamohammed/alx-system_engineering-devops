#!/usr/bin/python3
"""records all tasks that are owned by this employee"""

if __name__ == "__main__":
    """records all tasks that are owned by this employee"""
    import requests
    import sys
    import csv

    fake_api = 'https://jsonplaceholder.typicode.com/'
    employee = requests.get(fake_api + "users/{}".format(sys.argv[1])).json()
    tasks = requests.get(fake_api + "todos", params={"userId": sys.argv[1]}).json()
    employee_username = user.get("username")
    
    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csv_file:
    csv_w = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    [csv_w.writerow([sys.argv[1], employee_username, task.get("completed"),
                     task.get("title")]) for task in tasks]
