with open('in', 'r') as f:
    file_str = f.read().strip()

nice = 0

for word in file_str.splitlines():
    lookup = {word[:2] : -1}
    double = False
    pair = False


    for i, (a, b, c) in enumerate(zip(word, word[1:], word[2:])):

        letters = b + c
        if letters in lookup:
            if i - lookup[letters] > 1:
                double = True
        
        else:
            lookup[letters] = i

        pair |= a == c

    if pair and double:
        nice += 1

print(nice)
