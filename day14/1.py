from parse import search, findall
from collections import Counter


with open('in', 'r') as f:
    file_str = f.read()

    start = search("{}\n", file_str)[0]

    rules = {r[0]: r[1] for r in findall("{:.2} -> {:1}", file_str)}


pair_counts = Counter()

for a, b in zip(start, start[1:]):
    pair_counts[a + b] += 1


for step in range(40):

    for k, v in list(pair_counts.items()):

        pair_counts[k[0] + rules[k]] += v
        pair_counts[rules[k] + k[1]] += v

        pair_counts[k] -= v

ans = Counter()

for k, v in Counter(pair_counts).items():
    ans[k[0]] += v
    ans[k[1]] += v

ans[start[0]] += 1
ans[start[-1]] += 1

for k in ans:
    ans[k] //= 2

print(max(ans.values()) - min(ans.values()))