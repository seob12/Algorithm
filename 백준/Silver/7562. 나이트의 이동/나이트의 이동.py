from collections import deque

t = int(input())

def in_range(x,y):
    return 0<=x<i and 0<=y<i

def bfs(i,j):
    q = deque()
    q.append((i,j))
    v[i][j] = 1
    global ans

    di = [2,2,1,1,-2,-2,-1,-1]
    dj = [-1,1,-2,2,-1,1,-2,2]

    while q:
        x,y = q.popleft()

        if x == con_x and y == con_y:
            return arr[x][y]

        for d in range(8):
            nx = x + di[d]
            ny = y + dj[d]

            if not in_range(nx,ny):
                continue
            else:
                if v[nx][ny] == 0 and arr[nx][ny] == 0:
                    q.append((nx,ny))
                    v[nx][ny] = 1
                    arr[nx][ny] = arr[x][y] + 1



for _ in range(t):
    i = int(input())
    arr = [[0]*i for _ in range(i)]
    v = [[0]*i for _ in range(i)]

    x,y = map(int,input().split())
    con_x, con_y = map(int,input().split())

    print(bfs(x,y))

