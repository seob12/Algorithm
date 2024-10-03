from collections import deque

n,m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
#visited = [[0]*m for _ in range(n)]
#result = 1e9

di = [0,0,1,-1]    #동서남북
dj = [1,-1,0,0]


def bfs(r_x,r_y,b_x,b_y):
    q = deque()
    q.append((r_x,r_y,b_x,b_y))
    visited = []
    visited.append((r_x,r_y,b_x,b_y))
    cnt = 0
    
    while q:
        for _ in range(len(q)):
            rx,ry,bx,by = q.popleft()  # 좌표를꺼내고

            if cnt > 10:
                print(-1)
                return

            if arr[rx][ry] == 'O':
                print(cnt)
                return

            for d in range(4):  # 4방향 탐색
                nrx, nry = rx, ry
                while 1:
                    nrx += di[d]
                    nry += dj[d]
                    #nbx += di[d]
                    #nby += dj[d]

                    if arr[nrx][nry] == '#':
                        nrx -= di[d]
                        nry -= dj[d]
                        break

                    if arr[nrx][nry] == 'O':
                        break

                nbx,nby = bx,by

                while 1:
                    nbx += di[d]
                    nby += dj[d]

                    if arr[nbx][nby] == '#':
                        nbx -= di[d]
                        nby -= dj[d]
                        break

                    if arr[nbx][nby] == 'O':
                        break

                if arr[nbx][nby] == 'O':
                    continue

                if nrx == nbx and nry == nby:
                    if abs(nrx-rx) + abs(nry - ry) > abs(nbx-bx) + abs(nby-by):
                        nrx -= di[d]
                        nry -= dj[d]
                    else:
                        nbx -= di[d]
                        nby -= dj[d]

                if (nrx,nry,nbx,nby) not in visited:
                    q.append((nrx,nry,nbx,nby))
                    #q.append((nbx,nby))
                    visited.append((nrx,nry,nbx,nby))
                
        cnt += 1
    print(-1)
        


for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            r_x,r_y = i,j
        if arr[i][j] == 'B':
            b_x,b_y = i,j
            
bfs(r_x,r_y,b_x,b_y)
#print(result)