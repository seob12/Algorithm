k,n,m = map(int,input().split())

snack = k*n

if snack <= m:
    print(0)
else:
    print(snack - m)