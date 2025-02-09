from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    v[start] = 1

    while q:
        x = q.pop()

        for i in range(n):
            if arr[x][i] and not v[i]:
                v[i] = 1
                q.append(i)


n = int(input())
m = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
plan = list(map(int, input().split()))


v = [0] * (n+1)

bfs(plan[0]-1)
ans = 'YES'

for k in plan:
    if not v[k-1]:
        ans = 'NO'
        break

print(ans)