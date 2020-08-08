import sys

if __name__ == "__main__":
    N, C = sys.stdin.readline().split(" ")
    N = int(N)
    C = int(C)
    
    houses = []
    for _ in range(N):
        houses.append(int(sys.stdin.readline()))
    
    houses.sort()
    routers = [houses[0], houses[N - 1]]
    for i in range(C):
        
    