import PIL.Image
import numpy as np
from bitstring import BitArray
from itertools import cycle
import wavio

flag = "flag{ti_kak_smiritelnuy_rubashku_snyal}"

bits = "10101010" + BitArray(flag.encode()).bin

st = PIL.Image.open("sticker.png")
st = st.convert("1")
st = np.array(st)
st = np.uint8(st) # Read sticker as 

ar = np.zeros(st.shape)
for i, c in zip(range(ar.shape[0]), cycle(bits)):
    if c == '1':
        ar[i] = (np.random.rand(*ar[0].shape) > 0.3)
    #for j in range(0, ar.shape[1], 20):
    #    ar[i][j] = i%2
    #for j in range(1, ar.shape[1], 20):
    #    ar[i][j] = not i%2

ar = np.uint8(ar)
res_ar = 1-np.bitwise_or(1-ar, st) # Resulting picture

#res_ar_255 = 255 * res_ar
#print(res_ar_255)
#img = PIL.Image.fromarray(res_ar_255)
#img = img.convert("1")
#img.show() # For debug

orig = wavio.read("song.wav")
orig_d = orig.data.flatten()*(32767/32768)
orig_d = np.int16(orig_d)
print(np.amin(orig_d), np.amax(orig_d))

res = np.resize(res_ar.flatten(), orig_d.shape)
new_d = orig_d.copy()
max_val = np.iinfo(orig_d.dtype).max
for i in range(orig_d.shape[0]):
    if res[i]:
        new_d[i] = max_val

print(np.amin(new_d), np.amax(new_d))
print(new_d.dtype)

wavio.write("task.wav", new_d, orig.rate)

