depth, distance = 0, 0

with open('in', 'r') as f:
    for line in f.read().splitlines():
        direction, amount = line.split()

        amount = int(amount)

        if direction == 'forward':
            distance += amount

        if direction == 'down':
            depth += amount

        if direction == 'up':
            depth -= amount

print(distance * depth)