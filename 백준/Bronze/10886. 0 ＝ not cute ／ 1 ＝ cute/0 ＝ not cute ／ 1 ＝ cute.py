n = int(input())

cnt_0 = 0
cnt_1 = 0

for _ in range(n):
    k = int(input())

    if k == 1:
        cnt_1 += 1
    else:
        cnt_0 += 1

if cnt_1 > cnt_0:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')