a,p = map(str,input().split())
p = int(p)

dp = [0] * 10010

dp[0] = a
ans = 1

def dfs(i):
    global ans

    total = 0
    s = []

    for idx in dp[i-1]:
        s.append(int(idx[0]))

    for k in s:
        total += (k**p)

    dp[i] = str(total)


for i in range(1,10001):
    dfs(i)

res = []

for m in dp:
    if m not in res:
        res.append(m)

    else:
        idx = dp.index(m)
        break

print(idx)