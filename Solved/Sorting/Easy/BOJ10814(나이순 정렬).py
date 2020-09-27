import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().split()[0])
    clients = list()
    for _ in range(N):
        age, name = sys.stdin.readline().split()
        clients.append([int(age), name])
    clients.sort(key = lambda x: x[0])
    for element in clients:
        print(element[0], element[1])