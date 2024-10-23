h,m = map(int,input().split())

cnt = 0

while 1:
    if cnt == 45:
        break

    m -= 1
    cnt += 1

    if m==-1:
        m = 59
        h -= 1

        if h == -1:
            h = 23

print(h, m)