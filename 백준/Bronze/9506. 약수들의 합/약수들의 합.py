def cx(n):
    cnt = 1
    arr = []
    target = 0

    for i in range(1,n):
        if n % i == 0:
            arr.append(i)

    arr.sort()
    s = ' + '.join(map(str, arr))

    if sum(arr) != n:
        print(f'{n} is NOT perfect.')
    else:
        print(f'{n} = {s}')


while 1:
    n = int(input())

    if n == -1:
        break
    else:
        cx(n)

