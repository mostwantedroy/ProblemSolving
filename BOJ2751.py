import sys

def quick_sort(left, right):
    i = left
    j = right
    pivot = arr[(i+j) // 2]
    while (i <= j):
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if (i <= j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
    
    if left < j:
        quick_sort(left, j)
    if i < right:
        quick_sort(i, right)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = []
    for _ in range(N):
        arr.append(int(sys.stdin.readline()))

    quick_sort(0, N - 1)
    for i in range(N):
        print(arr[i])