from Crypto.Util.number import isPrime
from math import sqrt
from gmpy2 import invert
#from megalib123ololo import factorize
xD = [int(i,16) for i in '614e797687|82955cdf44|1e8ad93f69|3fd1bca826|60aced459b|1e1f267421|82955cdf44|1e1f267421|82955cdf44|1e1f267421|1db373a8d9'.split('|')]
pub = 1867939819429

known = ord('f')

lol = known*pub - xD[0]

#pri = max(factorize(lol)) #[3,3,3,7,1005883244291] 
pri = 1005883244291

kek = invert(pub, pri)
print(''.join(chr(i*kek % pri) for i in xD))
