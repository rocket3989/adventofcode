counts = [0 for _ in range(12)]

arr = []

with open('in', 'r') as f:
    for line in f.read().splitlines():
        arr.append(line)


        for i, c in enumerate(line.split()):
            if c == '1':
                counts[i] += 1


