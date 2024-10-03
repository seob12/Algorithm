import itertools

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [0 for _ in range(N)]
result = 1e9


def dfs(idx,L):
    global result
    if L == N//2:
        a = 0
        b = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    a += arr[i][j]
                elif visited[i] == 0 and visited[j] ==0:
                    b += arr[i][j]

        result = min(result, abs(a-b))
        return
    
    for i in range(idx,N):
        if not visited[i]:
            visited[i] = 1
            dfs(i+1,L+1)
            visited[i] = 0

dfs(0,0)
print(result)
