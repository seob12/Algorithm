def dfs(start,next,total,v):
    global ans

    if 0 not in v:
        if arr[next][start] > 0:
            ans = min(ans, total + arr[next][start])
        return

    for i in range(n):
        if v[i] == 0 and arr[next][i] > 0 and total < ans:
            v[i] = 1
            dfs(start,i,total + arr[next][i],v)
            v[i] = 0


n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
ans = 1e9

for i in range(n):
    visited = [0] * n
    visited[i] = 1
    dfs(i,i,0,visited)

print(ans)