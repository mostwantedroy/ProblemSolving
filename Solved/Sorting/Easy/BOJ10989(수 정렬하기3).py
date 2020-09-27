import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    
    counting = [0 for i in range(10000)]
    for _ in range(N):
        number = int(sys.stdin.readline())
        counting[number - 1] += 1
    
    for i in range(10000):
        if counting[i] != 0:
            for _ in range(counting[i]):
                print(i + 1)
        