import sys
from itertools import combinations, permutations

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for _ in range(N):
        number = int(sys.stdin.readline())
        numbers = [str(i) for i in range(1, number + 1)]
        
        plus = ['+'] * (number - 1)
        minus = ['-'] * (number - 1)
        merge = [' '] * (number - 1)

        char = plus + minus + merge
        operator = list(set(list(combinations(char, number - 1))))

        operator_new = []
        for i in range(len(operator)):
            for j in list(permutations(operator[i], number - 1)):
                operator_new.append(j)
        operator_new = list(set(operator_new))
        length = len(operator_new)
        
        answer = []
        for i in range(length):
            string = "".join(list(map(lambda x, y: x + y, numbers, operator_new[i]))) + numbers[-1]
            compute = string.replace(" ","")
            if eval(compute) == 0:
                answer.append(string)
        answer.sort()
        for i in answer:
            print(i)
        print()