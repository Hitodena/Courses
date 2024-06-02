sum = 0
mid = 0
array = [float(input("Значение -> ")) for i in range(int(input("Количество символов -> ")))]
for i in range(len(array)):
    sum += array[i]
    mid = sum / len(array)
# highest = max(array)
# lowest = min(array)
highest = array[0]
lowest = array[0]
for i in range(len(array)):
    if array[i] > highest:
        highest = array[i]   
    if array[i] < lowest:
        lowest = array[i]
print(f"Количество чисел в массиве: {len(array)}")
print(f"Среднее арифметическое: {mid}")
print(f"Наибольшее: {highest}")
print(f"Наименьшее: {lowest}")