import itertools

n = int(input())
num = list(map(int,input().split()))
num.sort()
cnt = 0

for i in range(n):
    lst = num[:i] + num[i+1:]

    left,right = 0, len(lst)-1
    
    while left < right:
        total = lst[left] + lst[right]
        
        if total == num[i]:
            cnt += 1
            break
        elif total < num[i]:
            left += 1
        else:
            right -= 1

print(cnt)
