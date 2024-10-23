t = int(input())


for _ in range(t):
    n = int(input())
    arr = dict()
    for i in range(n):
        s,k = map(str,input().split())
        arr[s] = int(k)
        
    sorted_arr = sorted(arr.items(),key = lambda x: x[1], reverse = True)

    print(sorted_arr[0][0])

