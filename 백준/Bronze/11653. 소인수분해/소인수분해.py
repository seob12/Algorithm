n = int(input())
cnt = 2

while n != 1:
    if n % cnt == 0:
        n = n // cnt
        print(cnt)
        cnt = 2
        
    else:
        cnt += 1
