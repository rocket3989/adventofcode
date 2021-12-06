p = []

moves = [int(i) for i in input().split(',')]

for i in range(100):
    input()
    mat = []
    for j in range(5):
        mat.append([int(x) for x in input().split()])

    p.append(mat)


best = []
best_score = 0

def score(grid):
    for row in grid:
        if sum(row) == 5:
            return True

    for i in range(5):
        if sum(grid[j][i] for j in range(5)) == 5:
            return True


def eval_grid(grid):
    state = [[0 for _ in range(5)] for _ in range(5)]
    for i, move in enumerate(moves, 1):
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == move:
                    state[r][c] = 1
                    if score(state):
                        return (state, move, i)
                        
for grid in p:
    state, move, i = eval_grid(grid)

    if i > best_score:
        best_score = i
        best = (grid, state, move)


count = 0
for r in range(5):
    for c in range(5):
        if best[1][r][c] == 0:
            count += best[0][r][c]


print(count * best[2])