p = int(input())
arr = []
ans = []

    
for i in range(1,p+1):
    arr = list(map(int, input().split()))
    result = 0
    arr.pop(0)
    for j in range(20):
        for k in range(j+1,20):
            if arr[j] > arr[k]:
                arr[j],arr[k] = arr[k],arr[j]
                result += 1
                
    print(i, result)