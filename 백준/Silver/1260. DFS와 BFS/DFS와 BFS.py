from collections import deque

def dfs(c):
    ans_dfs.append(c)
    visited[c] = 1

    for k in arr[c]:
        if not visited[k]:
            dfs(k)


def bfs(k):
    q = deque()
    q.append(k)
    ans_bfs.append(k)
    visited[k] = 1

    while q:
        x = q.popleft()

        for n in arr[x]:
            if not visited[n]:
                q.append(n)
                ans_bfs.append(n)
                visited[n] = 1




n,m,v = map(int,input().split())

arr = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)

for i in range(1,n+1):
    arr[i].sort()

visited = [0]*(n+1)
ans_dfs=[]
dfs(v)

visited = [0]*(n+1)
ans_bfs= []
bfs(v)

print(*ans_dfs)
print(*ans_bfs)
