n = int(input())
sw = list(map(int,input().split()))
sw.insert(0, 'No')
ans=[]

k = int(input())

def in_range(x):
    return 1 <= x < n+1

def change(idx):
    if sw[idx] == 0:
        sw[idx] = 1
    else:
        sw[idx] = 0

for _ in range(k):
    sex, num = map(int,input().split())

    if sex == 1:  # 남자
        for i in range(1,n+1):
            if i % num == 0:
                change(i)

    elif sex == 2:  # 여자
        change(num)

        for i in range(n // 2):
            if num-i < 1 or num+i > n:
                break
            if sw[num-i] == sw[num+i]:
                change(num-i)
                change(num+i)
            else:
                break





for a in range(1,n+1):
    print(sw[a], end=' ')
    if a % 20 == 0:
        print()