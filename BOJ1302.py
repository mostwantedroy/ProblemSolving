import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    sold = dict()
    for _ in range(N):
        book = sys.stdin.readline().split()[0] 
        if book in sold:
            sold[book] += 1
        else:
            sold[book] = 1
    sold_list = sorted(sold.items(), key = lambda x: (-x[1], x[0]))
    print(sold_list[0][0])