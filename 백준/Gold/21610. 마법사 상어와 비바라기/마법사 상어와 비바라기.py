from collections import deque
import copy

n,m = map(int, input().split())
arr = []
#tmp = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

goorm = []

for _ in range(m):
    d,s = map(int,input().split())
    goorm.append((d,s))
    
def in_range(x,y):
    return 0 <= x < n and 0 <= y < n
    
di = [0,-1,-1,-1,0,1,1,1]   # 8개
dj = [-1,-1,0,1,1,1,0,-1]
q = deque()
    
biba = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]

for d,s in goorm:
    cloud = []
    for x,y in biba:      # 구름이동 후 1줄임
        vec_1 = di[d-1] * s
        vec_2 = dj[d-1] * s
        
        nx = (x + vec_1) % n
        ny = (y + vec_2) % n
        arr[nx][ny] += 1
        
        cloud.append((nx,ny))
        
    for x,y in cloud:
        cnt = 0
        for nx,ny in ((x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)):
            if in_range(nx,ny) and arr[nx][ny] > 0:
                cnt += 1

        arr[x][y] += cnt
        
    new = []
    
    for i in range(n):
        for j in range(n):
            if (i,j) not in cloud and arr[i][j] >= 2:  # 구름이 있던 칸 제외하고 2이상이면
                arr[i][j] -= 2
                new.append((i,j))
    biba = new
        
    
result = 0

for i in range(n):
    for j in range(n):
        result += arr[i][j]
        
        
        
print(result)