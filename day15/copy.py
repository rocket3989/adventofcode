
mat = []

with open('in', 'r') as f:
    for line in f.read().splitlines():
        mat.append([int(x) for x in line])

outmat = []

for row in range(5):
    for r in mat:
        temp = []
        for column in range(5):
            for val in r:
                el = (val + row + column)

                while el > 9:
                    el -= 9
                temp.append(el)

        outmat.append(temp)

for row in outmat:
    print(*row, sep='')