import sys

def calculate(cables, limit):
    count = 0
    for cable in cables:
        count += cable // limit

    return count

if __name__ == '__main__':
    K, N = map(int, sys.stdin.readline().split())

    cables = []
    for _ in range(K):
        cables.append(int(sys.stdin.readline()))

    left = 1
    right = max(cables)

    while left <= right:
        mid = (left + right) // 2

        count = calculate(cables, mid)

        if count < N:
            right = mid - 1
        else:
            left = mid + 1

    print(right)