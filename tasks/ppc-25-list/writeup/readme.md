## Таск: Странный список
_Серфя вконтач вы нашли странную группу. В ней был один файл, структура которого уж очень напоминает csv, но что делать с ним вам не понятно._

## Writeup:
Нам дан csv файл с тремя столбцами x, y и c. x и y повсеместно используются для обозначения координат. Будем воспринимать эти два столбца как координаты для третьего столбца. 
  
Прочтем файл и составим массив:
```python
lines = []
with open("file.csv") as f:
    f.readline()  # пропустит первую строчку
    for line in f:
        line = line.strip().split(",")  # Убирает лишний \n на конце строки и делит всю строку по запятой
        lines.append((int(line[0]), int(line[1]), line[2]))

print(lines)
```
```>>> [(20, 3, '0'), (11, 12, '0'), (28, 26, '0'), (3, 14, '1')...```
  
Сделаем матрицу, заполним её и выведем
```python
# Чтобы все данные вместились надо найти максимальные x и y-ки
# т.к. все данные >=0 нам не нужно заморачиваться с отрицательными индексами
max_x = max([i[0] for i in lines])
max_y = max([i[1] for i in lines])

arr = [[' ' for j in range(max_y+1)] for i in range(max_x+1)]  # Создаем матрице размерами max_x+1, max_y+1

for x, y, c in lines:  # Заполняем
    arr[x][y] = c

print(arr) 
```
```
>>>
[['1', '1', '1', '1', '1', '1', '1', '0', ...], ['1', '0', '0', '0', '0', '0', '1', '0'...]
```
Обратите внимание на 1111111 в начале и 1000001 во второй строке. Это наталкивает на мысль о том, что эта матрица представляет qr код, ведь именно так устроен qr код. Выведем всю матрицу построчно.

```python
print('\n'.join(''.join(i) for i in arr))  # Выведем как матрицу
``` 
```
>>>
11111110100110000000001111111
10000010101110011010101000001
10111010111011100000001011101
10111010010000110110001011101
10111010010111001101101011101
10000010100101000100101000001
11111110101010101010101111111
00000000100101101111000000000
...
```
Да, это действительно qr код. Явно видны все четыре маркера для его определения. Чтобы его отсканировать нужно представить его в виде картинки. Достаточно поставить в терминале квадратный шрифт и заменить все нолики пробелами, а единички полными блоками из таблицы unicode. Отсканируем qr код с экрана с помощью телефона. Если у вас нет телефона, просто сделайте скриншот того, что напишется в терминале и отправьте это в любой онлайн сканер qr кодов.  
Я это сделал и вот что у меня получилось:  
![QR](qr.png)  
Этот qr код сканируется с телефона и мы видим флаг: flag{b4sica1ly_a_png}. Если у вас не получалется, попробуйте сканировать эту картинку на черном фоне. Для того чтобы некоторые сканеры смогли найти маркеры им нужно, чтобы вокруг маркера был цвет фона.