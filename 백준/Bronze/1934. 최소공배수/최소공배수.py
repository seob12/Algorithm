p = int(input())

for _ in range(p):
    a,b = map(int,input().split())
    aa,bb = a,b

    while bb != 0:
        aa = aa%bb
        aa,bb = bb,aa

    print(a*b//aa)