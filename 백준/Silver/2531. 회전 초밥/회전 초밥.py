import itertools

n,d,k,c = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(int(input()))

res = []
ans = -1

for i in range(0,n):
    lst = []
    for cnt in range(i,i+k):
        lst.append(arr[cnt%n])
    array = list(set(lst))

    if c in array:
        ans = max(ans, len(array))
    else:
        ans = max(ans, len(array) + 1)
    #res.append(lst)

print(ans)