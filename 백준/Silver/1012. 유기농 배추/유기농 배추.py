from collections import deque

t = int(input())

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs(i,j):
    q = deque()
    q.append((i,j))
    v[i][j] = 1

    di = [0,0,1,-1]
    dj = [1,-1,0,0]

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]

            if not in_range(nx,ny):
                continue
            else:
                if arr[nx][ny] == 1 and v[nx][ny] == 0:
                    v[nx][ny] = 1
                    q.append((nx,ny))



for _ in range(t):
    m,n,k = map(int,input().split())
    cnt = 0

    arr = [[0]*m for _ in range(n)]
    v = [[0]*m for _ in range(n)]

    for _ in range(k):
        y,x = map(int,input().split())

        arr[x][y] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and v[i][j] == 0:
                bfs(i,j)
                cnt += 1

    print(cnt)
