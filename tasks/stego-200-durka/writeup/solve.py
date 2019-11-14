import numpy as np
import wavio

a = wavio.read("task.wav").data
print(np.max(a), np.min(a))
b = (a == 32767).flatten()

b = np.resize(b, (342, 512))
# b = np.uint8(b)
# b *= 255
# from PIL import Image
# img = Image.fromarray(b)
# img.show()

s = ''.join([("1" if np.sum(i) else "0") for i in b])

while len(s) % 8:
    s += "0"

import bitstring
print(bitstring.BitArray(bin=s).bytes)
