mat = []

with open('in', 'r') as f:
    for line in f.read().splitlines():
        mat.append([int(x) for x in line])

N = len(mat)
M = len(mat[0])

adj = [[] for i in range(N * M + 1)]
values = [0 for i in range(N * M)]


for r in range(N):
    for c in range(M):
        values[c + r * N] = mat[r][c]

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            R = dr + r
            C = dc + c

            if R >= N or C >= M or C < 0 or R < 0:
                continue

            adj[c + r * N].append(C + R * N)

from collections import deque


count = 0
for step in range(1000):

    Q = deque()

    for i in range(N * M):
        values[i] += 1

        if values[i] == 10:
            Q.append(i)

    
    flashed = set()

    
    while Q:
        flash = Q.popleft()

        flashed.add(flash)
        for other in adj[flash]:
            values[other] += 1

            if values[other] == 10:
                Q.append(other)
            
        
    for flash in flashed:
        count += 1
        values[flash] = 0


    if len(flashed) == N * M:
        print(step + 1)
        

print(count)