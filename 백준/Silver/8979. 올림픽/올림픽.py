n,k = map(int,input().split())
arr = []

for _ in range(1,n+1):
    arr.append(list(map(int,input().split())))

arr.sort(key =lambda x: (-x[1], -x[2], -x[3]))

for i in range(n):
    if arr[i][0] == k:
        idx = i
for j in range(n):
    if arr[idx][1:] == arr[j][1:]:
        print(j+1)
        break



