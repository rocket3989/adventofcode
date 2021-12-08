from collections import Counter

with open('in', 'r') as f:
    for line in f.read().splitlines():
        fish = [int(x) for x in line.split(',')]

        c = Counter(fish)

        for i in range(256):
            a = Counter()

            for k, v in c.items():

                if k == 0:
                    a[6] += v
                    a[8] += v
                
                else:
                    a[k - 1] += v

            c = a

        print(sum(c.values()))
