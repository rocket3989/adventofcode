

dots = []
folds = []

with open('in', 'r') as f:
    for line in f.read().splitlines():
        try:
            x, y = [int(x) for x in line.split(',')]
            dots.append((x, y))

        except:
            try:
                direction, fold = line.split('=')

                folds.append((direction[-1], int(fold)))
            except:
                pass


seen = set()

for x, y in dots:
    for direction, fold in folds:

        if direction == 'x':
            if x > fold:
                x = fold - (x - fold)

        if direction == 'y':
            if y > fold:
                y = fold - (y - fold)

    seen.add((x, y))


matrix = [[' ' for _ in range(40)] for _ in range(6)]

for x, y in seen:
    matrix[y][x] = '#'

for row in matrix:
    print(*row)