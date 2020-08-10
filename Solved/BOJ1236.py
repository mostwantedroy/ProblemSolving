import sys

def search(i, N):
    for j in range(N):
        if "X" == castle[j][i]:
            return True
    return False


if __name__ == "__main__":
    N, M = sys.stdin.readline().split(" ")
    N = int(N)
    M = int(M)

    castle = []
    for i in range(N):
        castle.append(sys.stdin.readline()[0:-1])
    print(castle[2][2])
    guard_N = 0
    guard_M = 0
    for i in range(N):
        if "X" not in castle[i]:
            guard_N += 1
    
    for i in range(M):
        if not search(i, N):
            guard_M += 1

    print(max(guard_N, guard_M))