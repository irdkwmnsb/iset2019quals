from binascii import unhexlify as u
ms = eval(open('output.txt', 'r').read())

print(u(hex(ms[0][0] + ms[1][2] + ms[2][1] + ms[3][3])[2:]))
