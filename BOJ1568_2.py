import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    count = 0
    i = 1
    while N > 0:
        if i > N:
            i = 1
        N -= i
        i += 1
        count += 1
    print(count)