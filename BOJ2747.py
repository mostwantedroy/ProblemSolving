import sys

def fibonacci(n, d):
    if n == 0 or n == 1:
        return d[n]
    elif d[n] != 0: 
        return d[n]
    else:
        d[n] = fibonacci(n - 1, d) + fibonacci(n - 2, d)
        return d[n]


if __name__ == "__main__":
    N = int(sys.stdin.readline().split()[0])
    
    d = [0, 1] + [0] * (N - 1)

    fibonacci(N , d)
    
    print(d[N])
    
    