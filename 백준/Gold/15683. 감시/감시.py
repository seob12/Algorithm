import copy


mode = [[],[[0],[1],[2],[3]],
        [[0,1], [2,3]],
        [[0,3],[0,2],[1,2],[1,3]],
        [[0,1,3],[0,2,3],[0,1,2],[1,2,3]],
        [[0,1,2,3]]]

di = [0,0,1,-1]
dj = [1,-1,0,0]

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cctv = []
ans = 1e9

for i in range(n):
    for j in range(m):
        if arr[i][j] in [1,2,3,4,5]:
            cctv.append((arr[i][j],i,j))
            
def in_range(x,y):
    return 0 <= x < n and 0 <= y < m
            
def fill(arr,mode,x,y):
    for k in mode:
        nx = x
        ny = y
        while 1:
            nx += di[k]
            ny += dj[k]  # 계속 이동
                
            if in_range(nx,ny):
                if arr[nx][ny] == 6:
                    break

                elif arr[nx][ny] == 0:
                    arr[nx][ny] = '#'
            else:
                break

def dfs(depth, arr):
    global ans
    
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
            
        ans = min(ans, count)
        return
    
    temp = copy.deepcopy(arr)
    num, x, y = cctv[depth]
    for i in mode[num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)
    

dfs(0, arr)
print(ans)
    
    