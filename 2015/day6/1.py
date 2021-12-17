from parse import search, findall



with open('in', 'r') as f:
    file_str = f.read().strip()

lights = [[0 for _ in range(1000)] for _ in range(1000)]

for raw in file_str.splitlines():
    instruction, *cords = search("{} {:d},{:d} through {:d},{:d}", raw)


    for row in range(cords[0], cords[2] + 1):
        for col in range(cords[1], cords[3] + 1):
            
            if instruction == 'turn on':
                lights[row][col] = 1
            
            if instruction == 'turn off':
                lights[row][col] = max(lights[row][col] - 1, 0)

            
            if instruction == 'toggle':
                lights[row][col] += 2
    

    
print(sum(sum(row) for row in lights))