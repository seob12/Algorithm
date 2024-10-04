from collections import deque

n,m,k = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dice_num = [1,2,3,4,5,6]

di = [0,1,0,-1]   # 동남서북
dj = [1,0,-1,0]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def bfs(i,j):
    cnt = 1
    q = deque()
    q.append((i,j))
    v = [[0]*m for _ in range(n)]
    v[i][j] = 1
    
    while q:
        x,y = q.popleft()
        
        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]
            
            if in_range(nx,ny) and arr[nx][ny] == arr[x][y] and v[nx][ny] == 0:
                cnt += 1
                q.append((nx,ny))
                v[nx][ny] = 1
                
    return cnt
    

d = 0
result = 0
x,y = 0,0
ans_1 = 0

for _ in range(k):
    if in_range(x+di[d],y+dj[d]):
        nx = x + di[d]
        ny = y + dj[d]
    else:
        d = (d+2)%4
        nx = x + di[d]
        ny = y + dj[d]
        
    if d == 0:
        dice_num = [dice_num[3]] + [dice_num[1]] + [dice_num[0]] + [dice_num[5]] + [dice_num[4]] + [dice_num[2]]
    elif d == 1:
        dice_num = [dice_num[1]] + [dice_num[5]] + [dice_num[2]] + [dice_num[3]] + [dice_num[0]] + [dice_num[4]]
    elif d == 2:
        dice_num = [dice_num[2]] + [dice_num[1]] + [dice_num[5]] + [dice_num[0]] + [dice_num[4]] + [dice_num[3]]
    elif d == 3:
        dice_num = [dice_num[4]] + [dice_num[0]] + [dice_num[2]] + [dice_num[3]] + [dice_num[5]] + [dice_num[1]]
        
    
    cnt = bfs(nx,ny)
            
    result += (arr[nx][ny] * cnt)
    
    if dice_num[5] > arr[nx][ny]:
        d = (d+1)%4
    elif dice_num[5] < arr[nx][ny]:
        d = (d-1)%4
    
    x = nx
    y = ny
        
        
print(result)