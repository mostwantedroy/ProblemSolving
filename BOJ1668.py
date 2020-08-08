import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    trophy = []
    for _ in range(N):
        trophy.append(int(sys.stdin.readline()))
    left = trophy[0]
    right = trophy[N - 1]

    count_left = 1
    count_right = 1
    print(trophy)
    for i in range(1, N):
        if trophy[i] > left:
            count_left += 1
            left = trophy[i]
    
    for i in range(N - 2, -1, -1):
        if trophy[i] > right:
            count_right += 1
            right = trophy[i]
    
    print(count_left)
    print(count_right)