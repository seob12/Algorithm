n,l = map(int,input().split())

lst = []
tmp = ['.'] * 1000001

for _ in range(n):
    lft,right = map(int,input().split())
    lst.append((lft,right))

lst.sort(key = lambda x:(x[0], x[1]))
ans = 0
cur = 0

for x,y in lst:
    if x > y:
        continue
    if cur > x:
        x = cur
    while x < y:
        x += l
        ans += 1

    cur = x

print(ans)