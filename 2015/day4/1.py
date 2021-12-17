import hashlib


for i in range(1, 10000000):
    if hashlib.md5(f'iwrupvqb{i}'.encode()).hexdigest()[:5] == '00000':
        print(i)
        break