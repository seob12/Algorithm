while 1:
    s,n = map(int, input().split())

    if s == 0 and n == 0:
        break

    if s % n == 0:
        print('multiple')
    elif n % s == 0:
        print('factor')

    else:
        print('neither')