lookup = dict(zip("()", [1, -1]))

with open('in', 'r') as f:
    file_str = f.read()
    floor = 0
    for char in file_str.strip():
        floor += lookup[char]

    print(floor)