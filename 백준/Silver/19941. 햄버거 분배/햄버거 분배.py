

n,k = map(int,input().split())

arr = list(input())


ans = 0

for i in range(n):
    if arr[i] == 'P':
        for j in range(i-k,i+k+1):
            if 0 <= j < n and arr[j] == 'H':
                ans += 1
                arr[j] = 1
                break

print(ans)