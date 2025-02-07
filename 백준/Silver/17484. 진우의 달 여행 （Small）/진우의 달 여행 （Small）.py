n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

def dfs(i,j,direction,mid,total):
    dir = [-1,0,1]

    if i == n-1:
        tmp = min(mid,total)
        return tmp

    for d in dir:
        if d == direction:
            continue
        else:
            nx = i + 1
            ny = j + d

            if 0<=nx<n and 0<=ny<m:
                mid = dfs(nx,ny,d,mid,total + arr[nx][ny])

    return mid


ans = 1e9
for j in range(m):
    ans = min(ans,dfs(0,j,-2,ans,arr[0][j]))

print(ans)