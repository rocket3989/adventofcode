depth, distance, aim = 0, 0, 0

with open('in', 'r') as f:
    for line in f.read().splitlines():
        direction, amount = line.split()

        amount = int(amount)

        if direction == 'forward':
            distance += amount
            depth += aim * amount

        if direction == 'down':
            aim += amount

        if direction == 'up':
            aim -= amount

print(distance * depth)