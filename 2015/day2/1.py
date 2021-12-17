from parse import search, findall
from itertools import combinations
from math import prod

with open('in', 'r') as f:
    file_str = f.read()

    data = [tuple(x for x in r) for r in findall("{:d}x{:d}x{:d}", file_str)]

area = 0

for present in data:
    smallest = float('inf')

    for comb in combinations(present, 2):
        area += prod(comb) * 2
        smallest = min(smallest, prod(comb))

    area += smallest
print(area)