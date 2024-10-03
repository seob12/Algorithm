from collections import deque

n,l,r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

di = [-1,0,1,0]    # 북동남서
dj = [0,1,0,-1]

for i in range(n):
    col = 0
    for j in range(len(arr[i])):
        col += 1
        

def in_range(x,y):
    return 0 <= x < n and 0 <= y < col

def bfs(i,j):
    q = deque()
    temp = []
    q.append((i,j))
    temp.append((i,j))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + di[i]
            ny = y + dj[i]
            
            if in_range(nx,ny) and visited[nx][ny] == 0:
                if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    temp.append((nx,ny))
                    
    return temp
    

result = 0
while 1:
    visited = [[0] * col for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(col):
            if visited[i][j] == 0:
                visited[i][j] = 1
                gook = bfs(i,j)
                
                if len(gook) > 1:
                    flag = 1
                    
                    num = sum([arr[x][y] for x,y in gook]) // len(gook)
                    
                    for x,y in gook:
                        arr[x][y] = num
                        
    if flag == 0:
        break
        
    result += 1
    
print(result)
                    
        


