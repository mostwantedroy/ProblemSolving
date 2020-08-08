import sys

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

if __name__ == "__main__":
    number_of_test = int(sys.stdin.readline().split()[0])
    for _ in range(number_of_test):
        relation = int(sys.stdin.readline().split()[0])

        parent = dict()
        number = dict()

        for i in range(relation):
            x, y = sys.stdin.readline().split()
            
            if x not in parent:
                parent[x] = x
                number[x] = 1
            if y not in parent:
                parent[y] = y
                number[y] = 1
            
            union(x, y)
            print(number[find(x)])
            
        
# introducing Union-Find Algorithm
'''
def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x

if __name__ == "__main__":
    parent = list()

    for i in range(5):
        parent.append(i)

    union(1, 4)
    union(2, 4)

    for i in range(1, 5):
        print(find(i), end = '')
     
    print(parent)

'''