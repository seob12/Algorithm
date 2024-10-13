a,b = map(int,input().split())
c = int(input())

while c > 0:
    b += 1
    c -= 1
    
    if b == 60:
        b = 0
        a += 1
        
    if a == 24:
        a = 0
        
print(a, b)