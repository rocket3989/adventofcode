from itertools import permutations

segments = [set('abcefg'),
            set('cf'),
            set('acdeg'),
            set('acdfg'),
            set('bcdf'),
            set('abdfg'),
            set('abdefg'),
            set('acf'),
            set('abcdefg'),
            set('abcdgf')
            ]

count = 0

with open('in', 'r') as f:
    for line in f.read().splitlines():

        all_numbers, numbers = line.split(' | ')

        for perm in permutations('abcdefg'):

            letter_mapping = {a: b for a, b in zip(perm, 'abcdefg')}

            input_mapping = {}

            for val in all_numbers.split():

                curr = set(letter_mapping[letter] for letter in val)

                for i, thing in enumerate(segments):
                    if thing == curr:
                        input_mapping[tuple(sorted(val))] = i
                        break

            if len(input_mapping) == 10:
                break

        ans = 0

        for word in numbers.split():
            ans *= 10
            ans += input_mapping[tuple(sorted(word))]

        count += ans

print(count)
