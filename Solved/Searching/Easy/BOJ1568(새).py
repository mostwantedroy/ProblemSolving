import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    count = 0
    birds = N
    i = 1
    while True:
        if birds == 0:
            print(count)
            break
        elif birds - i < 0:
            i = 1
        else:
            birds -= i
            count += 1
            i += 1