from itertools import permutations

with open('in', 'r') as f:
    lines = f.read().splitlines()


class Node():
    left = None
    right = None
    value = None
    parent = None
    root = False

    def __init__(self, parent=None):
        self.parent = parent

    def __repr__(self):
        if self.value is not None:
            return str(self.value)

        return f'[{self.left}, {self.right}]'


def search_expl(node, depth):

    if node.value is not None: return False

    if depth >= 4 and node.left.value is not None and node.right.value is not None:

        curr = node

        while curr.root is False and curr.parent.left is curr:
            curr = curr.parent

        if not curr.root:
            curr = curr.parent.left

            if curr.value is not None:
                curr.value += node.left.value

            else:
                while curr.right.value is None:
                    curr = curr.right
                
                curr.right.value += node.left.value
    

        curr = node
        while curr.root is False and curr.parent.right is curr:
            curr = curr.parent

        if not curr.root:
            curr = curr.parent.right

            if curr.value is not None:
                curr.value += node.right.value
            
            else:
                while curr.left.value is None:
                    curr = curr.left

                curr.left.value += node.right.value

        node.left = None
        node.right = None
        node.value = 0

        return True


    if search_expl(node.left, depth + 1): return True
    if search_expl(node.right, depth + 1): return True

    return False

def search_split(node):

    if node.value is not None:
        if node.value > 9:
            node.left = Node(node)
            node.left.value = node.value // 2

            node.right = Node(node)
            node.right.value = (1 + node.value) // 2

            node.value = None
        
            return True

        return False

    if search_split(node.left): return True
    if search_split(node.right): return True

    return False

def reduce(root):
    while True:
        if search_expl(root, 0): 
            continue

        if search_split(root): 
            continue

        break
    return root

root = None

def tree_from_line(line):
    root = Node()
    curr = root
    for char in line:
        if char == '[':
            curr.left = Node(curr)
            curr = curr.left

        elif char == ']':
            
            curr = curr.parent
        
        elif char == ',':
            curr = curr.parent
            curr.right = Node(curr)
            curr = curr.right

        else:
            curr.value = int(char)
    
    return root

for line in lines:

    if root is None:
        root = tree_from_line(line)
        root.root = True
    
    else:
        newRoot = Node()
        newRoot.left = root
        root.parent = newRoot
        root.root = False
        root = newRoot
        root.root = True
        root.right = tree_from_line(line)
        root.right.parent = root

    root = reduce(root)


def mag(node):
    if node.value is not None: return node.value

    return 3 * mag(node.left) + 2 * mag(node.right)

print(root)
print(mag(root))

best = 0
for a, b in permutations(lines, 2):
    root = Node()
    root.root = True

    root.left = tree_from_line(a)
    root.right = tree_from_line(b)

    root.left.parent = root
    root.right.parent = root

    best = max(best, mag(reduce(root)))

print(best)