from collections import deque
import itertools

n = int(input())

arr = list(map(int,input().split()))

cnt = 0

s = list(itertools.permutations(arr,n))

for i in s:
    ans = 0
    for j in range(n-1):
        ans += abs(i[j] - i[j+1])

    cnt = max(cnt, ans)


print(cnt)