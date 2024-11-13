from collections import deque

n,k = map(int,input().split())

def in_range(x):
    return 0 <= x <= 100000

def bfs():
    q = deque()
    v = [0] * 100001
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            return v[k]

        for i in (x-1,x+1,2*x):
            if in_range(i) and not v[i]:
                v[i] = v[x] + 1
                q.append(i)


print(bfs())