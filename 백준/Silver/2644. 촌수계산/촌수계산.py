n = int(input())

a,b = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

v = [0] * (n+1)

def dfs(x, count):
    global flag
    v[x] = 1

    if x == b:
        flag = 1
        print(count)

    for val in graph[x]:
        if not v[val]:
            dfs(val,count + 1)



flag = 0
dfs(a,0)

if flag == 0:
    print(-1)