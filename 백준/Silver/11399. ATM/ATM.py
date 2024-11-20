import itertools

n = int(input())
arr = list(map(int,input().split()))

arr.sort()
ans = 1e9

cnt = 0
first = arr[0]
cnt += first
for j in range(1,n):
    first += arr[j]
    cnt += first

ans = min(ans, cnt)


print(ans)