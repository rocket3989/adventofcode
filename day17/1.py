targx = (139, 187)
targy= (-148, -89)

count = 0

for initalvx in range(1, 500):
    for initalvy in range(-500, 500):

        highest = 0
        vx = initalvx
        vy = initalvy

        x, y = 0, 0

        while x <= targx[1] and y >= targy[0]:
        
            x += vx
            y += vy

            if vx > 0:
                vx -= 1
            if vx < 0:
                vx += 1

            vy -= 1

            highest = max(highest, y)

            if targx[0] <= x <= targx[1] and targy[0] <= y <= targy[1]:
                count += 1
                break
        
print(count)