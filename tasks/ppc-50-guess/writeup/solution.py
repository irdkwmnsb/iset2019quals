import nclib

nc = nclib.Netcat(("localhost", 33003))
nc.read_line()
flag = ""
while True:
    nc.read_line()
    l, r = 0, 256
    while True:
        m = (r + l) // 2
        print(l, m, r)
        nc.read_until(b">")
        nc.sendln(str(m).encode())
        resp = nc.read_line().decode()
        print(resp)
        if "Correct" in resp:
            flag += chr(m)
            break
        elif "higher" in resp:
            l = m
        elif "lower" in resp:
            r = m
        else:
            print("??")
            break
    print(flag)
print(flag)
