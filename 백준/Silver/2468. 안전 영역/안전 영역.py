from collections import deque

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

max_num = 0

for i in range(n):
    for j in range(n):
        max_num = max(max_num, arr[i][j])

def bfs(i,j,value,v):
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
                if arr[nx][ny] > value and not v[nx][ny]:
                    v[nx][ny] = 1
                    q.append((nx,ny))


ans = 0

for i in range(max_num):
    v = [[0]*n for _ in range(n)]
    cnt = 0

    for x in range(n):
        for y in range(n):
            if arr[x][y] > i and v[x][y] == 0:
                bfs(x,y,i,v)
                cnt += 1

    ans = max(ans, cnt)

print(ans)