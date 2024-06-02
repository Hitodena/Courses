import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(response.text)

todos_by_user = {}  # {1: 10, }

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            todos_by_user[todo['userId']] = 1
print(todos_by_user)

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print(top_users)

max_complete = top_users[0][1]
print(max_complete)

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))
print(users)

max_users = " and ".join(users)
print(max_users)
print(f"Users {max_users} completed {max_complete} TODOS")


def keep(todo):
    completed = todo["completed"]
    max_count = str(todo["userId"]) in users
    return completed and max_count


with open("filter_file.json", "w") as f:
    filtered = list(filter(keep, todos))
    json.dump(filtered, f, indent=2)
