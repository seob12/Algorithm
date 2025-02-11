from collections import deque

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs(i,j,k):
    q = deque()
    q.append((i,j,k,0))
    v = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
    v[0][0][k] = 1

    while q:
        x,y,k,move = q.popleft()

        if x == n-1 and y == m-1:
            return move

        if k > 0:
            di_k = [-1,-1,-2,-2,1,1,2,2]
            dj_k = [-2,2,-1,1,-2,2,-1,1]

            for d in range(8):
                nx = x + di_k[d]
                ny = y + dj_k[d]

                if in_range(nx,ny) and not v[nx][ny][k-1] and arr[nx][ny] == 0:
                    q.append((nx,ny,k-1,move+1))
                    v[nx][ny][k-1] = 1


        di = [0,0,1,-1]
        dj = [1,-1,0,0]

        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]

            if in_range(nx,ny) and arr[nx][ny] == 0 and not v[nx][ny][k]:
                q.append((nx,ny,k,move+1))
                v[nx][ny][k] = 1

    return -1






k = int(input())
m,n = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

print(bfs(0,0,k))
