from collections import deque

n,m = map(int,input().split())


arr = [list(map(int,input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]

di = [0,0,1,-1]
dj = [1,-1,0,0]

picture = 0
draw = 0
lst = [0]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def bfs(x,y):
    global picture
    q = deque()
    q.append((x,y))
    v[x][y] = 1
    cnt = 1

    while q:
        r,c = q.popleft()

        for d in range(4):
            nx = r + di[d]
            ny = c + dj[d]

            if not in_range(nx,ny):
                continue
            else:
                if arr[nx][ny] == 1 and v[nx][ny] == 0:
                    v[nx][ny] = 1
                    cnt += 1
                    q.append((nx,ny))

    lst.append(cnt)



for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and v[i][j] == 0:
            bfs(i,j)
            draw += 1



print(draw)
print(max(lst))
