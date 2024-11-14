from collections import deque

n = int(input())
node = int(input())

graph = [[] for _ in range(n+1)]
v = [0] * (n+1)

for _ in range(node):
    a,b = map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]

def bfs():
    q = deque([1])
    v[1] = 1

    while q:
        x = q.popleft()

        for nx in graph[x]:
            if v[nx] == 0:
                q.append(nx)
                v[nx] = 1

bfs()

print(sum(v)-1)