import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().split()[0])
    numbers = list()
    for i in range(N):
        numbers.append(int(sys.stdin.readline().split()[0]))
    numbers.sort()
    
    for number in numbers:
        print(number)