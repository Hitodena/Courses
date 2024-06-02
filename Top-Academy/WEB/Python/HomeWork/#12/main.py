data = {}
avg = 0
count = 0

qu = int(input("Количество студентов: "))

for el in range(1, qu + 1):
    student = input(f"{el}-й студент: ")
    score = int(input("Балл: "))
    data.update({student:score})
    avg += data[student]
    count += 1

average = round(avg / count)
cool = []

for key, value in data.items():
    if value > average:
        cool.append(key)

print(f"Средний балл: {average}. Студенты с баллов выше среднего:")
for i in cool:
    print(i)






