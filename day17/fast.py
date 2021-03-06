from collections import defaultdict

targx = (117, 7310)
targy= (-9546, -89)
count = 0


y_answers = defaultdict(set)

for initalvy in range(2*targy[0], 2*-targy[0]):

    vy = initalvy

    y = 0

    for step in range(500):
        y += vy
        vy -= 1

        if targy[0] <= y <= targy[1]:
            y_answers[step].add(initalvy)
        
        if y < targy[0]:
            break


for initalvx in range(targx[1] + 1):

    vx = initalvx

    x = 0

    successful = set()

    for step in range(500):
    
        x += vx

        if vx > 0:
            vx -= 1

        if targx[0] <= x <= targx[1]:
            successful |= y_answers[step]

        if x > targx[1]:
            break
    
    count += len(successful)

print(count)

