from collections import deque

f,s,g,u,d = map(int,input().split())
visited = [0 for _ in range(f+1)]
count = [0 for _ in range(f+1)]

def bfs():
    q = deque([s])
    visited[s] = 1

    while q:
        x = q.popleft()

        if x == g:
            return count[g]

        for i in (x+u, x-d):
            nx = i
            if 0<nx<=f and visited[nx]==0:
                visited[nx] = 1
                q.append(nx)
                count[nx] = count[x] + 1

    return -1



c = bfs()

if c == -1:
    print('use the stairs')
else:
    print(c)