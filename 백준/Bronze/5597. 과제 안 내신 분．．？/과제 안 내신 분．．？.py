v = [0]*30

for _ in range(28):
    n = int(input())

    v[n-1] = 1
    
for i in range(30):
    if v[i] == 0:
        print(i+1)