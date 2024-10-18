from collections import deque

problem = 0

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def bfs(x,y,arr,cost):
    #cnt = 0
    q = deque()
    q.append((x,y))
    cost[x][y] = arr[x][y]
    #v = [[0 for _ in range(n)]for _ in range(n)]
    #cnt += arr[x][y]

    di = [0,0,1,-1]
    dj = [1,-1,0,0]

    while q:
        r,c = q.popleft()

        #v[r][c] = 1
        #dir = []

        for d in range(4):
            nx = r + di[d]
            ny = c + dj[d]

            if in_range(nx,ny):
                if cost[nx][ny] > cost[r][c] + arr[nx][ny]:
                    cost[nx][ny] = cost[r][c] + arr[nx][ny]
                    q.append((nx,ny))


    return cost



while 1:
    n = int(input())
    ans = 0
    if n == 0:
        break

    problem += 1
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))

    cost = [[1e9]*n for _ in range(n)]

    ans = bfs(0,0,arr,cost)

    print(f'Problem {problem}: {ans[n-1][n-1]}')