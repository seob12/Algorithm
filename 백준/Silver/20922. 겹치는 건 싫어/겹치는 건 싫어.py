from collections import defaultdict

n,k = map(int,input().split())

arr = list(map(int,input().split()))

count = defaultdict(int)
ans = -1
left, right = 0,0

while right < n:
    if count[arr[right]] < k:
        count[arr[right]] += 1
        right += 1
    else:
        count[arr[left]] -= 1
        left += 1
    ans = max(ans, right - left)

print(ans)