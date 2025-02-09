arr = list(input())

ans = 1e9

for i in range(len(arr)):
    cnt = 0
    for j in range(arr.count('a')):
        idx = (i+j)%len(arr)

        if arr[idx] == 'b':
            cnt += 1
    ans = min(ans, cnt)

print(ans)
