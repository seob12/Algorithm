t = int(input())

def dfs(idx):
    if v[idx] == 0:
        v[idx] = 1
        dfs(arr[idx])

    return





for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.insert(0,0)
    v = [0]*(n+1)
    ans = 0

    for i in range(1,n+1):
        if v[i] == 0:
            ans += 1
            dfs(i)

    print(ans)
    