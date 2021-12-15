from parse import search, findall
from collections import Counter
import numpy as np
from numpy.linalg import matrix_power


with open('in', 'r') as f:
    file_str = f.read()

    start = search("{}\n", file_str)[0]

    rules = [(r[0], r[1]) for r in findall("{:.2} -> {:1}", file_str)]


letters = set(char for char in file_str if char.isalpha())

letter_index = {letter: i for i, letter in enumerate(letters)}

letter_count = len(letters)

def letters_to_index(letters, count):
    return count * letter_index[letters[0]] + letter_index[letters[1]]


state = np.zeros(letter_count * letter_count, dtype=np.float64)


for a, b in zip(start, start[1:]):
    state[letters_to_index(a + b, letter_count)] += 1


transition = np.zeros((letter_count * letter_count, letter_count * letter_count), dtype=np.float64)


for source, dest in rules:
    transition[letters_to_index(source, letter_count), letters_to_index(source[0] + dest, letter_count)] = 1
    transition[letters_to_index(source, letter_count), letters_to_index(dest + source[1], letter_count)] = 1


transition = matrix_power(transition, 10**3)

state = np.matmul(state, transition)

ans = Counter((start[0], start[-1]))

for letter_pair, _ in rules:
    ans[letter_pair[0]] += int(state[letters_to_index(letter_pair, letter_count)])
    ans[letter_pair[1]] += int(state[letters_to_index(letter_pair, letter_count)])

print((max(ans.values()) - min(ans.values())) // 2)