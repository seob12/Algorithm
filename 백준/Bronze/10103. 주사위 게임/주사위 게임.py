n = int(input())

arr = []

for _ in range(n):
    i,j = map(int, input().split())
    arr.append((i,j))

a = 100
b = 100

for k in range(n):
    x,y = arr.pop(0)

    if x == y:
        continue
    elif x > y:
        b -= x

    elif x < y:
        a -= y

print(a)
print(b)



