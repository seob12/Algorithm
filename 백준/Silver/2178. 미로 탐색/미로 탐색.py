from collections import deque

n,m = map(int,input().split())

arr = [list(map(int,input())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
cnt = 1e9

di = [0,0,1,-1]
dj = [1,-1,0,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs(x,y):
    q = deque()
    v[x][y] = 1
    q.append((x,y))

    while q:
        i,j = q.popleft()

        for d in range(4):
            nx = i + di[d]
            ny = j + dj[d]

            if not in_range(nx,ny):
                continue
            else:
                if v[nx][ny] == 0 and arr[nx][ny] == 1:
                    arr[nx][ny] = arr[i][j] + 1
                    v[nx][ny] = 1
                    q.append((nx,ny))

    return arr[n-1][m-1]


re = bfs(0,0)


print(re)