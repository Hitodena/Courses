# import pickle
#
#
# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, stake):
#         self.__dict__ = stake
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# print(item1)
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)


import json
from random import choice

# data = {
#     'name': 'Ольга',
#     'age': 20,
#     20: None,
#     True: 1,
#     'hobbies': ('running', 'singing'),
#     'children': ['Alice', 'Bob']
# }
#
# with open('data_file.json', 'w') as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)
#
# with open('data_file.json') as f:
#     data1 = json.load(f)

# json_string = json.dumps(data, ensure_ascii=False)
# print(json_string)
# print(type(json_string))
# data1 = json.loads(json_string)
# print(data1)
# print(type(data1))


# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
# def write_json(person_list):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_list)
#     with open("persons.json", 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        # a = ''
        # for i in self.marks:
        #     a += str(i) + ", "
        a = ", ".join(map(str, self.marks))
        return f"Студент: {self.name} => {a[:-2]}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, ind):
        self.marks.pop(ind)

    def edit_mark(self, ind, nm):
        self.marks[ind] = nm

    def average(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def get_file_name(self):
        return self.name.lower() + ".json"

    def dump_to_json(self):
        data = {'name': self.name, "marks": self.marks}
        with open(self.get_file_name(), 'w') as f:
            json.dump(data, f)

    def load_from_file(self):
        with open(self.get_file_name()) as f:
            print(json.load(f))


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        a = "\n".join(map(str, self.students))
        return f"Группа: {self.group}\n{a}"

    def add_student(self, stud):
        self.students.append(stud)

    def remove_student(self, ind):
        self.students.pop(ind)

    @staticmethod
    def change_group(gr1, gr2, index):
        gr2.add_student(gr1.remove_Student(index))

    def get_file_name(self):
        return self.group.lower().replace(" ", "-") + ".json"

    def dump_to_json(self):
        data = [
            {'name': student.name, "marks": student.marks} for student in self.students
        ]
        with open(self.get_file_name(), "w") as f:
            json.dump(data, f, indent=2)

    def load_from_file(self):
        with open(self.get_file_name()) as f:
            print(json.load(f))


st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
# st1.dump_to_json()
# st2.dump_to_json()
# st1.load_from_file()
# st2.load_from_file()
sts1 = [st1, st2]
sts2 = [st2]
gr = Group(sts1, "ГК Python")
print(gr)
gr2 = Group(sts2, "ГК WEB")
print(gr2)
