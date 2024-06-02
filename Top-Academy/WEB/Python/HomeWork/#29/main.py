import json
from random import choice


def gen_person():
    ids = ''
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    while len(ids) != 15:
        ids += choice(nums)

    person = {
        ids: {
            'name': name,
            'tel': tel
            }
    }

    return person


def write_json(person_list):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = {}

    data.update(person_list)

    with open("persons.json", 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
