from collections import deque

m,n = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]

ans = 0

di = [0,0,1,-1]
dj = [1,-1,0,0]

q = deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs():
    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]

            if in_range(nx,ny) and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx,ny))


for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i,j))

bfs()

for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    ans = max(ans, max(i))

print(ans-1)


