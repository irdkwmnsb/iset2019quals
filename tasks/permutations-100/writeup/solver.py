e1, e2, e3 = [i[:-1] for i in open('output.txt', 'r').readlines()]

dick = {}

for i in range(len(e1)):
    dick[i] = []
    for j in range(len(e2)):
        if e2[j] == e3[i]:
            dick[i].append(j)
arr = []
for i in range(10):
    arr.append([])
    for j in range(len(e1)):
        if len(dick[j]) > i:
            arr[i].append(e1[dick[j][i]])
        else:
            arr[i].append('*')

for i in arr:
    print(*i)
