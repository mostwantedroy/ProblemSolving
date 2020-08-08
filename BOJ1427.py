import sys


# IT WAS COUNTING SORT !!!

if __name__ == "__main__":
    N = sys.stdin.readline().split()[0]
    order = [0 for i in range(10)]
    for char in N:
        order[int(char)] += 1
    
    answer = ""
    for i in range(9, -1, -1):
        answer += (str(i) * order[i])

    print(answer)
        




# 1st Trial : Success but I coundn't understand the problem. 
'''
import sys

if __name__ == "__main__":
    N = sys.stdin.readline().split()[0]
    numbers = list(map(int, list(N)))
    numbers.sort(reverse = True)
    numbers = list(map(str, list(numbers)))
    print("".join(numbers))
'''

# NDB's solution
'''
array = input()

for i in range(9, -1, -1):
    for j in array:
        if int(j) == i:
            print(i, end = '')

'''