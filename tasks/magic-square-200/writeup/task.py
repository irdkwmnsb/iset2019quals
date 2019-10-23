from random import randint
from copy import deepcopy as copy

flag = 0x666c61677b6974735f6e6f745f6d616769637d

square = [[0]*4, [0]*4, [0]*4, [0]*4]

def magic(square):
    magic_square = copy(square)

    for i in range(4):
        magic_square[0][i] += square[1][i]
        magic_square[1][i] += square[0][i]
        magic_square[2][i] += square[3][i]
        magic_square[3][i] += square[2][i]
    
    magic_square[0][0] += square[3][0] + square[0][1]
    magic_square[0][1] += square[0][0] + square[0][2]
    magic_square[0][2] += square[0][1] + square[0][3]
    magic_square[0][3] += square[0][2] + square[3][3]

    magic_square[1][0] += square[1][1] + square[1][3] + square[2][2]
    magic_square[1][1] += square[1][0] + square[2][3] + square[2][1]
    magic_square[1][2] += square[2][0] + square[2][2]
    magic_square[1][3] += square[1][0] + square[2][1]

    magic_square[2][0] += square[1][2] + square[2][3]
    magic_square[2][1] += square[1][1] + square[1][3]
    magic_square[2][2] += square[1][0] + square[1][2] + square[2][3]
    magic_square[2][3] += square[1][1] + square[2][0] + square[2][2]

    magic_square[3][0] += square[0][0] + square[3][1]
    magic_square[3][1] += square[3][0] + square[3][2]
    magic_square[3][2] += square[3][1] + square[3][3]
    magic_square[3][3] += square[3][2] + square[0][3]

    return magic_square
   
s = 0
for i in range(4):
    for j in range(4):
        square[i][j] = randint(0, flag // 16)
        s += square[i][j]

square[3][3] += flag - s

magic_square = magic(square)
out = open('output.txt', 'w')
out.write(str(magic_square))
out.close()





