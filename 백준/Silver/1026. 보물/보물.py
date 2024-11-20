n = int(input())

arr = list(map(int,input().split()))
lst = list(map(int, input().split()))

arr.sort()
lst.sort(reverse=True)
ans = 0

for i in range(n):
    a = arr[i] * lst[i]

    ans += a

print(ans)