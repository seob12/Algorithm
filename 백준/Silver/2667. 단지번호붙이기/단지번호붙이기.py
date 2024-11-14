from collections import deque

n = int(input())

arr = [list(map(int,input())) for _ in range(n)]

v = [[0]*n for _ in range(n)]
ans = []

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def bfs(x,y):
    q = deque()

    q.append((x,y))
    v[x][y] = 1
    res = 1

    while q:
        r,c = q.popleft()

        di = [0,0,1,-1]
        dj = [1,-1,0,0]

        for d in range(4):
            nx = r + di[d]
            ny = c + dj[d]

            if in_range(nx,ny) and v[nx][ny] == 0 and arr[nx][ny] == 1:
                q.append((nx,ny))
                v[nx][ny] = 1
                res += 1

    return res


cnt = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and v[i][j] == 0:
            r = bfs(i,j)
            cnt += 1
            ans.append(r)

print(cnt)

ans.sort()

for i in ans:
    print(i)