import sys

N, r, c = sys.stdin.readline().split(' ')
N = int(N)
r = int(r)
c = int(c)
count = 0

def visit(N, X, Y):
    N = N // 2
    global count
    
    if N > 1:
        visit(N, X, Y)
        visit(N, X, Y + N)
        visit(N, X + N, Y)
        visit(N, X + N, Y + N)
    else:
        if X == r and Y == c:
            print(count)
            return
        count += 1
        if X == r and Y + 1== c:
            print(count)
            return
        count += 1
        if X + 1 == r and Y == c:
            print(count)
            return
        count += 1
        if X + 1 == r and Y + 1 == c:
            print(count)
            return
        count += 1

if __name__ == "__main__":
    visit(2 ** N, 0, 0)
