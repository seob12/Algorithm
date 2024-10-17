n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

#arr.insert(0, [0]*m)
#arr.append([0]*m)

def dfs(col, row, d, low, answer):  # 백트래킹
    dir = [-1,0,1]

    if col == n-1:
        return min(low, answer)

    for i in dir:
        if i != d:
            if 0 <= col < n and 0 <= row + i < m:
                low = dfs(col+1, row+i, i, low, answer+arr[col+1][row+i])
    return low



low = 1e9
for i in range(m):
    low = min(dfs(0,i,2,low,arr[0][i]), low)

print(low)
