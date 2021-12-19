from parse import search, findall
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations

with open('in', 'r') as f:
    scanners = f.read().split('\n\n')

scanners = [[(r[0], r[1], r[2]) for r in findall("{:d},{:d},{:d}", scanner)] for scanner in scanners]

beacons = set(scanners[0])

scanner_nodes = set()
scanner_nodes.add((0, 0, 0))

unplaced = deque(scanners[1:])


def o_shift(point, orientation, perm, offset = (0, 0, 0)):
    point = tuple(a * b for a, b in zip(point, orientation))

    point = tuple(point[a] for a in perm)

    point = tuple(a + b for a, b in zip(point, offset))

    return point


def place_scanner(curr_scanner, beacons, scanner_nodes):
    for orientation in ((1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)):
        for perm in permutations(range(3)):
            for beacon in curr_scanner:

                beacon = o_shift(beacon, orientation, perm)

                for set_beacon in beacons:

                    offset = tuple(a - b for a, b in zip(set_beacon, beacon))

                    matched = set()
                    matched.add(set_beacon)

                    for other_beacon in curr_scanner:
                        other_beacon = o_shift(other_beacon, orientation, perm, offset)

                        for scanner_node in scanner_nodes:
                            for a, b in zip(other_beacon, scanner_node):
                                if abs(a - b) > 1000:
                                    break
                            else:
                                break
                        else:
                            continue

                        if other_beacon not in beacons:
                            break

                        matched.add(other_beacon)
                    
                    if len(matched) >= 12:
                        beacons |= set(o_shift(other_beacon, orientation, perm, offset) for other_beacon in curr_scanner)

                        scanner_nodes.add(offset)
                        return True
    return False

print('begining placement')

while unplaced:
    curr_scanner = unplaced.popleft()

    if place_scanner(curr_scanner, beacons, scanner_nodes):
        print('placed scanner')
        continue

    unplaced.append(curr_scanner)

print(len(beacons))

big = 0
for a, b in combinations(scanner_nodes, 2):

    curr = 0
    for a, b in zip(a, b):
        curr += abs(a - b)

    big = max(big, curr)

print(big)