n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
v = [[0]*m for _ in range(n)]
sm = 0
d = [(1,0),(-1,0),(0,1),(0,-1)]
    
def in_range(x,y):
    return 0 <= x < n and 0 <= y < m
    

def dfs(i,j,total,n):
    global sm
    
    if n == 4:
        sm = max(sm, total)
        return
    
    for di, dj in d:
        nx = i + di
        ny = j + dj
        
        if in_range(nx,ny) and v[nx][ny] == 0:
            if n == 2:
                v[nx][ny] = 1
                dfs(i,j,total + arr[nx][ny], n+1)
                v[nx][ny] = 0
            
            
            v[nx][ny] = 1
            dfs(nx,ny,total + arr[nx][ny], n+1)
            v[nx][ny] = 0
    
    
    

    
for i in range(n):
    for j in range(m):
        if v[i][j] == 0:
            v[i][j] = 1
            dfs(i,j,arr[i][j],1)
            v[i][j] = 0
            
print(sm)
