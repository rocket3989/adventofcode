from parse import parse, findall

dots = []
folds = []

with open('in', 'r') as f:
    file_str = f.read()

    dots = [(r[0], r[1]) for r in findall("{:d},{:d}", file_str)]

    folds = [(r[0], r[1]) for r in findall("{:1}={:d}",file_str)]


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