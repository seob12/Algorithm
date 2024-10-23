
n,m = map(int,input().split())

arr = [list(map(str,input())) for _ in range(n)]
ans = 0
tmp = set()
tmp.add((arr[0][0]))

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def dfs(x,y,count):
    global ans
    di = [0,0,1,-1]
    dj = [1,-1,0,0]

    ans = max(ans, count)

    for d in range(4):
        nx = x + di[d]
        ny = y + dj[d]

        if in_range(nx,ny) and arr[nx][ny] not in tmp:
            tmp.add(arr[nx][ny])
            dfs(nx,ny,count+1)
            tmp.remove(arr[nx][ny])



dfs(0,0,1)
print(ans)







