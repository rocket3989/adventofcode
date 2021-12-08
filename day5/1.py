grid = [[0 for _ in range(1001)] for _ in range(1001)]

with open('in', 'r') as f:
    for line in f.read().splitlines():
        a, b = line.split(' -> ')

        x1, y1 = [int(x) for x in a.split(',')]

        x2, y2 = [int(x) for x in b.split(',')]


        if x1 == x2:

            if y1 > y2:
                y1, y2 = y2, y1

            for y in range(y1, y2 + 1):
                grid[y][x1] += 1

        elif y1 == y2:

            if x1 > x2:
                x1, x2 = x2, x1


            for x in range(x1, x2 + 1):
                grid[y1][x] += 1

        elif abs(x1 - x2) == abs(y1 - y2):


            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            print(x1, y1, x2, y2)

            for diff in range(x2 - x1 + 1):

                if y1 < y2:
                    grid[y1 + diff][x1 + diff] += 1

                else:
                    
                    grid[y1 - diff][x1 + diff] += 1
                  
count = 0

for row in grid:
    for val in row:
        if val > 1:
            count += 1

for row in grid:
    for val in row:
        print(val if val > 0 else '.', end='')
    print()


print(count)