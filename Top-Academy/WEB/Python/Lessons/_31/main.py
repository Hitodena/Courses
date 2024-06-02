# import json
#
#
# class CountryCapital:
#     @staticmethod
#     def load(file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#         finally:
#             return data
#
#     @staticmethod
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столицы: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         data[new_country] = new_capital
#
#         with open(file_name, "w") as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print({k.capitalize(): v.capitalize() for k, v in json.load(f).items()})
#
#     @staticmethod
#     def delete_country(file_name):
#         del_country = input("Введите название страны: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         if del_country in data:
#             del data[del_country]
#
#             with open(file_name, "w") as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print("Такой страны в базе нету")
#
#     @staticmethod
#     def search_data(file_name):
#         country = input("Ведите название страны: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             print(f"Страна: {country.capitalize()} столица {data[country].capitalize()} есть в словаре")
#         else:
#             print(f"Страны {country.capitalize()} нету в словаре")
#
#     @staticmethod
#     def edit_data(file_name):
#         country = input("Введите страну для корректировки: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             new_cap = input("Введите новое значение столицы: ").lower()
#             data[country] = new_cap
#             with open(file_name, "w") as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print("Такой страны в базе нету")
#
#
# file = "list_capital.json"
# while True:
#     index = input("Выбор действия\n1 - Добавление данных\n2 - Удаление данных\n3 - Поиск данных\n"
#                   "4 - Редактирование данных\n5 - Просмотр данных\n6 - Завершение работы\nВвод: ")
#     if index == "1":
#         CountryCapital.add_country(file)
#     elif index == "2":
#         CountryCapital.delete_country(file)
#     elif index == "3":
#         CountryCapital.search_data(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("Введен некорректный номер")


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
print(f"Users {max_users} completed {max_complete} TODO")
