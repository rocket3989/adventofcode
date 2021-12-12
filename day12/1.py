from collections import defaultdict
adj = defaultdict(list)

with open('in', 'r') as f:
    for line in f.read().splitlines():
        u, v = line.strip().split('-')
        adj[u].append(v)
        adj[v].append(u)

count = [0]

def dfs(seen, node, visited_2):

    if node == 'end':
        return 1

    if node.islower() and node != 'start':
        if seen[node] == 2:
            return 0
        
        if visited_2 and seen[node] == 1:
            return 0

        seen[node] += 1

        if seen[node] == 2:
            visited_2 = True
    
    
    count = 0

    for other in adj[node]:

        if other == 'start': continue
        count += dfs(seen, other, visited_2)

    if node in seen:
        seen[node] -= 1
    
    return count

print(dfs(defaultdict(int), 'start', False))