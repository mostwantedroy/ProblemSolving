import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    bricks = [(0, 0, 0, 0)]
    
    for i in range(1, N + 1):
        area, height, weight = map(int, sys.stdin.readline().split())
        bricks.append((area, height, weight, i))
    
    bricks.sort(key = lambda x:x[2])
    
    dp = [0] * (N + 1)
        
    for i in range(1, N + 1):
        for j in range(0, i):
            if bricks[i][0] > bricks[j][0]:
                dp[i] = max(dp[i], dp[j] + bricks[i][1])

    max_height = max(dp)
    index = N
    result = []
    
    while index != 0:
        if max_height == dp[index]:
            result.append(bricks[index][3])
            max_height -= bricks[index][1]
        index -= 1
    
    result.reverse()
    print(len(result))
    [print(i) for i in result]

                
            
        


    
    