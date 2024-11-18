m,n,k = map(int,input().split())
from collections import deque

arr = [[0]*m for _ in range(n)]
v = [[0]*m for _ in range(n)]

for _ in range(k):
    a,b,c,d = map(int,input().split())

    for i in range(a,c):
        for j in range(b,d):
            arr[i][j] = -1

def in_range(x,y):
    return 0<=x<n and 0<=y<m

res = []

def bfs(i,j):
    q = deque()
    q.append((i,j))
    v[i][j] = 1

    di = [0,0,1,-1]
    dj = [1,-1,0,0]

    cnt = 1

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]

            if not in_range(nx,ny):
                continue
            else:
                if arr[nx][ny] == 0 and v[nx][ny] == 0:
                    v[nx][ny] = 1
                    q.append((nx,ny))
                    cnt += 1

    res.append(cnt)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and v[i][j] == 0:
            bfs(i,j)

print(len(res))
res.sort()
for i in res:
    print(i,end=' ')