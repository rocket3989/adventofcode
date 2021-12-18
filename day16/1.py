import math
with open('in', 'r') as f:
    for line in f.read().splitlines():
        num = bin(int(line, 16))[2:].zfill(len(line) * 4)


class bits:
    fp = 0
    def get_bits(self, diff):
        ans = int(num[self.fp:self.fp + diff], 2)
        self.fp += diff
        return ans


b = bits()

function_lookup = [lambda x: sum(x), 
                    lambda x: math.prod(x), 
                    lambda x: min(x),
                    lambda x: max(x),
                    0,
                    lambda x: 1 if x[0] > x[1] else 0,
                    lambda x: 1 if x[0] < x[1] else 0,
                    lambda x: 1 if x[0] == x[1] else 0]


def eval_bits():
    ver = b.get_bits(3)
    
    type_ID = b.get_bits(3)
    
    package_length = 6

    if type_ID == 4:
        val = 0

        while True:
            package_length += 5
            header = b.get_bits(1)

            val *= 16
            
            val += b.get_bits(4)
            
            if header == 0:
                break

        return (package_length, val)
        
    
    else:
        header = b.get_bits(1)
        
        children = []


        if header == 0:
            sub = b.get_bits(15)
            
            package_length += 16 + sub

            count = 0
            while count < sub: 
                length, val = eval_bits()

                count += length
                children.append(val)
        
        else:
            sub = b.get_bits(11)
            
            package_length += 12

            for _ in range(sub):
                length, val = eval_bits()
                children.append(val)
                package_length += length
        
        return package_length, function_lookup[type_ID](children)

print(eval_bits()[1])