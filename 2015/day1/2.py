lookup = dict(zip("()", [1, -1]))

with open('in', 'r') as f:
    file_str = f.read()
    floor = 0
    for pos, char in enumerate(file_str.strip(), 1):
        floor += lookup[char]
        if floor == -1:
            print(pos)
            break