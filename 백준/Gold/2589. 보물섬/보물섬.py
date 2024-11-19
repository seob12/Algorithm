from collections import deque

n,m = map(int,input().split())

arr = [list(map(str,input())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs(i,j):
    q = deque()
    q.append((i,j))
    v[i][j] = 1

    di = [0,0,1,-1]
    dj = [1,-1,0,0]

    cnt = 0

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]

            if not in_range(nx,ny):
                continue
            else:
                if arr[nx][ny] == 'L' and v[nx][ny] == 0:
                    v[nx][ny] = v[x][y] + 1
                    q.append((nx,ny))
                    cnt = max(cnt, v[nx][ny])

    return cnt-1



ans = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            v = [[0] * m for _ in range(n)]
            c = bfs(i,j)
            ans = max(ans, c)

print(ans)