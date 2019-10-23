from Crypto.Util.number import getPrime

flag = 'flag{ololo}'

pri = getPrime(40)
pub = 1867939819429

m = [ord(i) for i in flag]
c = [hex(i*pub % pri)[2:] for i in m]

out = open('output.txt', 'w')
out.write('|'.join(c))
out.close()

