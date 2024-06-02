data = {
    "John" : {
        "N": 3056,
        "S": 8463,
        "E": 8441,
        "W": 2694
    },
    "Tom" : {
        "N": 4892,
        "S": 6786,
        "E": 4737,
        "W": 3612
    },
    "Anne" : {
        "N": 5239,
        "S": 4802,
        "E": 5828,
        "W": 1859
    },
    "Fiona" : {
        "N": 3904,
        "S": 3645,
        "E": 8821,
        "W": 2451
    }
}

for el in data:
    print(el)
    for subel in data[el]:
        print(f"{subel}: {data[el][subel]}")

name = input("Имя --> ")
region = input("Регион --> ")
print(data[name][region])

newp = int(input("Новое значение: "))
data[name][region] = newp

print(data[name])

