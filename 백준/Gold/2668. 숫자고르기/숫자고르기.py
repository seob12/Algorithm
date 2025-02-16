def dfs(depth,i):
    visited[depth] = 1
    w = arr[depth]

    if not visited[w]:
        dfs(w,i)
    elif visited[w] and w == i:
        res.append(w)

    #for i in range(1,n+1):


n = int(input())

arr = [0] + [int(input()) for _ in range(n)]

#v = [0] * n

res = []

for i in range(1,n+1):
    visited = [0] * (n+1)
    dfs(i,i)

print(len(res))
res.sort()

for i in res:
    print(i)