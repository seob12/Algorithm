t = int(input())

for _ in range(t):
    r, s = map(str, input().split())

    r = int(r)
    arr = list(map(str,s))
    ans = ''

    for i in range(len(arr)):
        ans += (arr[i] * r)

    print(ans)