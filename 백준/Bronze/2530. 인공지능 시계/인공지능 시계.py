a,b,c = map(int,input().split())
m = int(input())

while m > 0:
    m -= 1
    c += 1
    
    if c == 60:
        b += 1
        c = 0
    if b == 60:
        a += 1
        b = 0
    if a == 24:
        a = 0
        
print(a, b, c)
