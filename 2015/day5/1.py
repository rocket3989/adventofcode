with open('in', 'r') as f:
    file_str = f.read().strip()

nice = 0

for word in file_str.splitlines():
    vowels = 0
    double = False

    if word[-1] in 'aeiou':
        vowels += 1

    for a, b in zip(word, word[1:]):
        if a in 'aeiou':
            vowels += 1
        
        double |= a == b

        if a + b in ('ab', 'cd', 'pq', 'xy'):
            break
    
    else: 
        if vowels >= 3 and double:
            nice += 1

print(nice)
