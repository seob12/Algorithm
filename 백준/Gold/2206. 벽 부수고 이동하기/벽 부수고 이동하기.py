from collections import deque

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs(i,j,k):
    q = deque()
    q.append((i,j,k))

    v = [[[0]*2 for _ in range(m)] for _ in range(n)]
    v[0][0][0] = 1

    di = [0,0,1,-1]
    dj = [1,-1,0,0]

    while q:
        x,y,cnt = q.popleft()

        if x == n-1 and y == m-1:
            return v[x][y][cnt]

        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]

            if not in_range(nx,ny):
                continue
            else:
                if arr[nx][ny] == 0 and v[nx][ny][cnt] == 0:
                    v[nx][ny][cnt] = v[x][y][cnt] + 1
                    q.append((nx,ny,cnt))
                elif arr[nx][ny] == 1 and cnt == 0:
                    q.append((nx,ny,1))
                    v[nx][ny][1] = v[x][y][0] + 1


    return -1



n,m = map(int,input().split())

arr = [list(map(int,input())) for _ in range(n)]

print(bfs(0,0,0))