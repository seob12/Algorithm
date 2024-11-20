from collections import deque
import copy

n = int(input())

arr = [list(map(str, input())) for _ in range(n)]

no = 0   # 아닌 사람
tr = 0   # 색약인 사람

def in_rangne(x,y):
    return 0<=x<n and 0<=y<n

def bfs(i,j,target):
    q = deque()
    v[i][j] = 1
    q.append((i,j))

    di = [0,0,1,-1]
    dj = [1,-1,0,0]

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]

            if not in_rangne(nx,ny):
                continue
            else:
                if arr[nx][ny] in target and v[nx][ny] == 0:
                    q.append((nx,ny))
                    v[nx][ny] = 1


red = 0
green = 0
blue = 0

v = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R' and v[i][j] == 0:
            bfs(i,j,'R')
            red += 1
        elif arr[i][j] == 'G'and v[i][j] == 0:
            bfs(i,j,'G')
            green += 1
        elif arr[i][j] == 'B'and v[i][j] == 0:
            bfs(i,j,'B')
            blue += 1

no = red+blue+green

v = [[0]*n for _ in range(n)]

tmp = copy.deepcopy(arr)

for i in range(n):
    for j in range(n):
        if tmp[i][j] == 'G':
            tmp[i][j] = 'R'

blue = 0
red_green = 0

for i in range(n):
    for j in range(n):
        if tmp[i][j] == 'B'and v[i][j] == 0:
            bfs(i,j,'B')
            blue += 1
        elif tmp[i][j] == 'R' and v[i][j] == 0:
            bfs(i,j,['R','G'])
            red_green += 1

tr = blue + red_green

print(no, tr)
