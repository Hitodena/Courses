from random import randint

tpl = tuple((randint(0, 10) for i in range(int(input("Введите количество элементов --> ")))))
print(tpl)

array = []


for el in tpl:
    if el in tpl and el not in array:
        array.append(el)
        count = tpl.count(el)
        print(f"Количество {el} - {count}")
