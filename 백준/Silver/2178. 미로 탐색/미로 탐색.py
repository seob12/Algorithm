from collections import deque

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs(i,j):
    #global ans
    q = deque()
    q.append((i,j))
    #v = [[0]*m for _ in range(n)]
    #v[i][j] = 1

    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    #cnt = 0

    while q:
        x,y = q.popleft()

        if x == n-1 and y == m-1:
            return arr[x][y]

        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]

            if not in_range(nx,ny):
                continue
            else:
                if arr[nx][ny] == 1:
                    q.append((nx,ny))
                    arr[nx][ny] = arr[x][y] + 1


n,m = map(int,input().split())

arr = [list(map(int,input())) for _ in range(n)]

print(bfs(0,0))