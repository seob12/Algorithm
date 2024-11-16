from collections import deque

m,n,h = map(int,input().split())

arr = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append((i,j,k))


di = [0,0,1,-1,0,0]
dj = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while q:
        z,x,y = q.popleft()

        for d in range(6):
            nz,nx,ny = z+dz[d], x+di[d], y+dj[d]

            if 0<=nz<h and 0<=nx<n and 0<=ny<m and arr[nz][nx][ny] == 0:
                q.append((nz,nx,ny))
                arr[nz][nx][ny] = arr[z][x][y] + 1


bfs()
ans = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                print(-1)
                exit(0)
            ans = max(ans, arr[i][j][k])

print(ans-1)

