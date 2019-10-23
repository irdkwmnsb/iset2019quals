from string import ascii_lowercase
from random import randint, shuffle

alp = ascii_lowercase + '{}_'

def permute(s):
    s = [*enumerate(s)]
    shuffle(s)
    key = [i[0] for i in s]
    enc = [i[1] for i in s]
    return ''.join(enc), key

def arrange(enc, key):
    dec = [0]*len(enc)
    for i in range(len(enc)):
        dec[key[i]] = enc[i]
    return ''.join(dec)

def rollingrollingrolling(s, key):
    return ''.join(alp[(alp.index(s[i]) + key[i]) % len(alp)] for i in range(len(s)))

def check(s):
    for i in s:
        if i not in alp:
            return False
    return True

flag = '<redacted>'

out = open('output.txt', 'w')

if check(flag):
    enc, key1 = permute(flag)
    e1 = enc
    out.write(enc + '\n')

    key2 = [randint(1,1337) for i in range(len(enc))]
    enc = rollingrollingrolling(enc, key2)
    e2 = enc
    out.write(enc + '\n')

    enc = arrange(enc, key1)
    e3 = enc
    out.write(enc + '\n')
    out.close()

else:
    out.write('ololo')
    out.close()
