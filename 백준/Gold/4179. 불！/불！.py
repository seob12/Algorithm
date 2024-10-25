from collections import deque

n,m = map(int,input().split())

map = [list(map(str,input())) for _ in range(n)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m


def hbfs():
    while h_q:
        x,y = h_q.popleft()

        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]

            if not in_range(nx,ny):
                print(human[x][y])
                return

            if map[nx][ny] == '#' or human[nx][ny]:
                continue
            if fire[nx][ny] and human[x][y] + 1 >= fire[nx][ny]:
                continue

            human[nx][ny] = human[x][y] + 1
            h_q.append((nx,ny))

    print('IMPOSSIBLE')
    return


def fbfs():
    while f_q:
        x, y = f_q.popleft()

        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]

            if not in_range(nx,ny):
                continue
            if map[nx][ny] == '#' or fire[nx][ny]:
                continue
            fire[nx][ny] = fire[x][y] + 1
            f_q.append((nx,ny))



fire = [[0]*m for _ in range(n)]
human = [[0]*m for _ in range(n)]
h_q = deque()
f_q = deque()

for i in range(n):
    for j in range(m):
        if map[i][j] == 'J':
            h_q.append((i,j))
            human[i][j] = 1
        elif map[i][j] == 'F':
            f_q.append((i,j))
            fire[i][j] = 1

fbfs()
hbfs()



