#! /usr/bin/python3

lines = []
with open("file.csv") as f:
    f.readline()  # пропустит первую строчку
    for line in f:
        line = line.strip().split(",")  # Убирает лишний \n на конце строки и делит всю строку по запятой
        lines.append((int(line[0]), int(line[1]), line[2]))

print(lines)

# Чтобы все данные вместились надо найти максимальные x и y-ки
# т.к. все данные >=0 нам не нужно заморачиваться с отрицательными индексами
max_x = max([i[0] for i in lines])
max_y = max([i[1] for i in lines])

arr = [[' ' for j in range(max_y+1)] for i in range(max_x+1)]

for x, y, c in lines:
    arr[x][y] = c

print('\n'.join(''.join(i) for i in arr))  # Выведем как матрицу

s = '\n'.join(''.join(i) for i in arr)
s = s.replace('0', ' ').replace('1', '█')

print(s)
