match = {'{':'}',
         '[':']',
         '(': ')',
         '<': '>'
}

{c:i for i, c in enumerate('([{<', 1)}

{a:b for a, b in zip('([{<', ')]}>')}

score = {'{':3,
         '(':1,
         '<': 4,
         '[': 2
}

c = []
with open('in', 'r') as f:
    for line in f.read().splitlines():
        invalid = False
        s = []
        for char in line:
            if char in match:
                s.append(char)
            
            else:
                if char == match[s[-1]]:
                    s.pop()
                
                else:
                    invalid = True
        
        if invalid: continue

        cs = 0

        for char in reversed(s):
            cs *= 5
            cs += score[char]

        print(cs)
        c.append(cs)

print(sorted(c)[len(c) // 2])