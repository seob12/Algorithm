n = int(input())

arr = list(map(int,input().split()))

arr.sort()

left,right = 0, n*2 - 1

res = 1e9

while left < right:
    res = min(res, arr[left] + arr[right])

    left += 1
    right -= 1

print(res)