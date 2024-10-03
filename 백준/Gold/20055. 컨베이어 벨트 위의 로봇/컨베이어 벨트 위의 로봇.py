from collections import deque

n,k = map(int, input().split())
arr = deque(list(map(int, input().split())))
robot = deque([0] * n)

ans = 0

while 1:
    ans += 1

    arr.rotate(1)
    robot.rotate(1)

    robot[n-1] = 0

    for i in range(n-2,-1,-1):
        if arr[i+1] >= 1 and robot[i+1] == 0 and robot[i] == 1:
            arr[i+1] -= 1
            robot[i+1] = 1
            robot[i] = 0
        
    robot[n-1] = 0

    
    if arr[0] != 0:
        robot[0] = 1
        arr[0] -= 1

    if arr.count(0) >= k:
        break

print(ans)

    