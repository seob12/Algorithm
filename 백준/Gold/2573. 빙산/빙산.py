import copy
from collections import deque

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

        cnt = 0

        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]

            if not in_range(nx,ny):
                continue
            else:
                if arr[nx][ny] == 0:
                    v[x][y] += 1

                if v[nx][ny] == 0 and arr[nx][ny] != 0:
                    q.append((nx,ny))
                    v[nx][ny] = 1


n,m = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

ans = 0

while 1:
    v = [[0] * m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and v[i][j] == 0:
                bfs(i,j)
                count += 1

    for i in range(n):
        for j in range(m):
            if v[i][j] != 0:
                arr[i][j] -= (v[i][j] - 1)
                if arr[i][j] < 0:
                    arr[i][j] = 0

    if count >= 2:
        print(ans)
        break

    if count == 0:
        print(0)
        break

    ans += 1


