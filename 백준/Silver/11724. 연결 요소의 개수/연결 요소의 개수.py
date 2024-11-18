import copy

n,m = map(int,input().split())

arr = [[] for _ in range(n+1)]
v = [0] * (n+1)

def dfs(idx):
    v[idx] = 1

    for k in arr[idx]:
        if v[k] == 0:
            v[k] = 1
            dfs(k)

for _ in range(m):
    x,y = map(int, input().split())

    arr[x].append(y)
    arr[y].append(x)


ans = 0

for i in range(1,n+1):
    if v[i] == 0:
        dfs(i)
        ans += 1

print(ans)