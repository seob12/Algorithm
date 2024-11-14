t = int(input())
ans = 0

for _ in range(t):
    arr = list(map(int, input().split()))

    arr.sort()

    if arr[0] == arr[1] and arr[1] == arr[2]:
        ans = max(ans,(arr[0]*1000)+10000)
    elif arr[0] == arr[1] and arr[1] != arr[2]:
        ans = max(ans,(arr[0]*100)+1000)
    elif arr[0] != arr[1] and arr[1] == arr[2]:
        ans = max(ans, (arr[1]*100)+1000)
    else:
        ans = max(ans, max(arr)*100)


print(ans)