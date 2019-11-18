import pyqrcode
import random

qr = pyqrcode.create('flag{b4sica1ly_a_png}')

arr = qr.code

with open("file.csv", "w") as csvfile:
    csvfile.write("x,y,c\n")
    lines = []
    for i, row in enumerate(arr):
        for j, cell in enumerate(row):
            lines.append("%s,%s,%s\n" % (i, j, cell))
    random.shuffle(lines)
    csvfile.writelines(lines)
