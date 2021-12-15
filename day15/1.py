from heapq import heappush, heappop

mat = []

with open('in2', 'r') as f:
    for line in f.read().splitlines():
        mat.append([int(x) for x in line])

N = len(mat)
M = len(mat[0])

adj = [[] for i in range(N * M + 1)]
values = [0 for i in range(N * M)]


for r in range(N):
    for c in range(M):
        values[c + r * N] = mat[r][c]

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            R = dr + r
            C = dc + c

            if R >= N or C >= M or C < 0 or R < 0:
                continue

            adj[c + r * N].append(C + R * N)


h = [(0, 0)]

seen = set()

while h:
    cost, node = heappop(h)

    if node in seen:
        continue

    if node == (N * M) - 1:
        print(cost)
        break

    seen.add(node)

    for other in adj[node]:
        heappush(h, (values[other] + cost, other))

