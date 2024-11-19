import itertools

n,m = map(int,input().split())

arr = []

for i in range(1,n+1):
    arr.append(i)

lst = list(itertools.combinations(arr,m))

if m == 1:
    for i in arr:
        print(i)
else:
    for i in lst:
        s = list(map(str, i))
        tmp = ' '.join(s)

        print(tmp)