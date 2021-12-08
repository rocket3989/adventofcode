arr = []
with open('in', 'r') as f:
    for line in f.read().splitlines():
        arr.append(int(line))

count = 0

for x, y in zip(arr, arr[1:]):
    if y > x: count += 1

print(count)