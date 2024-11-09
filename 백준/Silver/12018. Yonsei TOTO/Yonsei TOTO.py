n,m = map(int,input().split())
ans = []

for _ in range(n):
    p, l = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort(reverse = True)

    if p < l:
        ans.append(1)
    else:
        ans.append(arr[l-1])

ans.sort()
count = 0

for i in ans:
    if m-i >= 0:
        count += 1
        m -= i

print(count)

