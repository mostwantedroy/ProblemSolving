import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().split()[0])
    points = list()
    
    for _ in range(N):
        x, y = sys.stdin.readline().split()
        points.append([int(x), int(y)])
    
    points.sort(key = lambda x: ( x[0], x[1] ))

    for point in points:
        print(point[0], point[1])