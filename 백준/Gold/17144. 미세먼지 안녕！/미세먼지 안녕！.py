from collections import deque

r,c,t = map(int, input().split())
array = []
for _ in range(r):
    array.append(list(map(int, input().split())))

for i in range(r):
    if array[i][0] == -1:
        up = i
        down = i+1
        break

def spread():
    di = [0,1,0,-1]   # 동남서북
    dj = [1,0,-1,0]

    tmp_arr = [[0]*c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if array[x][y] > 0:
                tmp = 0
                for dir in range(4):
                    nx = x + di[dir]
                    ny = y + dj[dir]

                    if 0 <= nx < r and 0 <= ny < c and array[nx][ny] != -1:
                        tmp_arr[nx][ny] += array[x][y] // 5
                        tmp += array[x][y] // 5
                
                array[x][y] -= tmp

    for i in range(r):
        for j in range(c):
            array[i][j] += tmp_arr[i][j]

    

def freshing():
    # 위쪽 공기청정기 순환
    x,y = up,1

    di = [0,-1,0,1]   # 동북서남
    dj = [1,0,-1,0]
    dir = 0
    before = 0

    while 1:
        nx = x + di[dir]
        ny = y + dj[dir]
        
        if x == up and y == 0:
            break

        if nx >= r or nx < 0 or ny >= c or ny < 0:
            dir += 1
            continue
        
        array[x][y], before = before, array[x][y]

        x = nx
        y = ny

def fresh_down():
    di = [0,1,0,-1]    # 동남서북
    dj = [1,0,-1,0]
    x,y = down,1
    dir = 0
    before = 0

    # 아래쪽 공기청정기 순환:
    while 1:
        nx = x + di[dir]
        ny = y + dj[dir]
        
        if x == down and y == 0:
            break

        if nx < 0 or nx >= r or ny >= c or ny < 0:
            dir += 1
            continue
        
        array[x][y], before = before, array[x][y]

        x = nx
        y = ny


for i in range(t):
    spread()
    freshing()
    fresh_down()

result = 0

for i in range(r):
    for j in range(c):
        if array[i][j] > 0:
            result += array[i][j]

print(result)
        
    

    