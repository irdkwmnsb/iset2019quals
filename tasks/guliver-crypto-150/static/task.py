from Crypto.Util.number import getPrime
from gmpy2 import powmod

flag = '<redacted>'
m = int.from_bytes(bytes(flag.encode('ascii')), 'big')

p = getPrime(1024)
n = p*p*p*p*p
e = 65537

c = powmod(m,e,n)
out = open('output.txt', 'w')
out.write(str(n) + '\n' + str(e) + '\n' + str(c))
out.close()
