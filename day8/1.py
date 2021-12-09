from itertools import permutations

segments = {frozenset('abcefg'): 0,
            frozenset('cf'): 1,
            frozenset('acdeg'): 2,
            frozenset('acdfg'): 3,
            frozenset('bcdf'): 4,
            frozenset('abdfg'): 5,
            frozenset('abdefg'): 6,
            frozenset('acf'): 7,
            frozenset('abcdefg'): 8,
            frozenset('abcdfg'): 9
            }

count = 0

with open('in', 'r') as f:
    for line in f.read().splitlines():

        all_numbers, numbers = line.split(' | ')

        for perm in permutations('abcdefg'):

            letter_mapping = {a: b for a, b in zip(perm, 'abcdefg')}

            input_mapping = {}

            for val in all_numbers.split():

                curr = frozenset(letter_mapping[letter] for letter in val)

                if curr in segments:
                    input_mapping[frozenset(val)] = segments[curr]

            if len(input_mapping) == 10:
                break

        ans = 0

        for word in numbers.split():
            ans *= 10
            ans += input_mapping[frozenset(word)]

        count += ans

print(count)
