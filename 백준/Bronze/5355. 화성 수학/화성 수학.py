n = int(input())

for _ in range(n):
    arr = list(map(str,input().split()))
    num = float(arr.pop(0))

    for i in arr:
        if i == '@':
            num *= 3
        elif i == '%':
            num += 5
        elif i == '#':
            num -= 7

    print("%0.2f" % num)

