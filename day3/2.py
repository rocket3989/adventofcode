arr = []
with open('in', 'r') as f:
    for line in f.read().splitlines():
        arr.append(line.strip())

o, c = 0, 0

arr1 = arr
for i in range(12):
    count = 0

    for val in arr1:
        if val[i] == '1':
            count += 1
    
    nextarr = []

    if count * 2 >= len(arr1):
        for val in arr1:
            if val[i] == '1':
                nextarr.append(val)
    else:
        for val in arr1:
            if val[i] == '0':
                nextarr.append(val)

    if len(nextarr) == 1:
        o = int(nextarr[0], 2)
        break

    arr1 = nextarr

for i in range(12):
    count = 0


    for val in arr:
        if val[i] == '1':
            count += 1
    
    nextarr = []

    if count * 2 < len(arr):
        for val in arr:
            if val[i] == '1':
                nextarr.append(val)
    else:
        for val in arr:
            if val[i] == '0':
                nextarr.append(val)

    if len(nextarr) == 1:
        print(nextarr[0])
        c = int(nextarr[0], 2)
        break
    
    print(arr)
    print(nextarr)
    arr = nextarr


print(o, c)
print(o * c)