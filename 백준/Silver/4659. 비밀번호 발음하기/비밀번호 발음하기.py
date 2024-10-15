arr = ['a','e','i','o','u']

while 1:
    n = input()
    chk,chk_1,chk_2 = 1,1,1

    if n == 'end':
        break

    count = 0
    for i in n:
        if i in arr:
            count += 1

    if count == 0:
        chk = 0
    else:
        chk = 1
    #print(chk)

    cnt_j = 0
    cnt_m = 0

    for i in n:
        if i in arr:
            cnt_m += 1  # 모음 카운트 증가
            cnt_j = 0
        elif i not in arr:
            cnt_j += 1
            cnt_m = 0

        if cnt_m == 3 or cnt_j == 3:
            chk_1 = 0
            break

    #print(chk_1)

    for j in range(len(n)-1):
        if n[j] == n[j+1]:
            chk_2 = 0
            if n[j] == 'e' and n[j+1] == 'e':
                chk_2 = 1
            elif n[j] == 'o' and n[j+1] == 'o':
                chk_2 = 1

    #print(chk_2)

    if chk and chk_1 and chk_2:
        print(f'<{n}> is acceptable.')
    else:
        print(f'<{n}> is not acceptable.')

