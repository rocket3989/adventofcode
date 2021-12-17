lookup = dict(zip('<>^v', ((-1, 0), (1, 0), (0, 1), (0, -1))))

with open('in', 'r') as f:
    file_str = f.read().strip()

position = [0, 0]

seen = set(((0, 0),))

for char in file_str[::2]:
    for i in range(2):
        position[i] += lookup[char][i]
    
    seen.add(tuple(position))

position = [0, 0]

for char in file_str[1::2]:
    for i in range(2):
        position[i] += lookup[char][i]
    
    seen.add(tuple(position))

print(len(seen))