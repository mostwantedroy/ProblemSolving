import sys

operator = []
operators = []

from copy import deepcopy

def generate(n):
    global operator
    global operators
    if len(operator) == n:
        operators.append(deepcopy(operator))
        return
    
    operator.append(" ")
    generate(n)
    operator.pop()
    
    operator.append("+")
    generate(n)
    operator.pop()

    operator.append("-")
    generate(n)
    operator.pop()

if __name__ == "__main__":
    test_case = int(sys.stdin.readline())
    
    for _ in range(test_case):
        operators = []
        operator = []
        N = int(sys.stdin.readline())
        generate(N - 1)
        numbers = [str(i) for i in range(1, N + 1)]
        for item in operators:
            expression = "".join(list(map(lambda x, y:x + y, numbers, item))) + numbers[-1]
            if eval(expression.replace(" ", "")) == 0:
                print(expression)
        print()