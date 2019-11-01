from random import randint
def encrypt(x):
    a = randint(1,133713371337)
    b = randint(1,133713371337)
    c = a*(x ** 2) + b*x
    return a, b, c

def main():
    flag = 'flag{u_g0t_a_5-plus_ma_bo1}'
    m = int.from_bytes(flag.encode('ascii'), "big")
    c = encrypt(m)
    print(c)

if __name__ == '__main__':
    main()
