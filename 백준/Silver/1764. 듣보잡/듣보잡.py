n,m = map(int,input().split())
arr = {input() for _ in range(n)}
ans = {input() for _ in range(m)}
res = []

for i in arr:
    if i in ans:
        res.append(i)

res.sort()

print(len(res))

for i in res:
    print(i)