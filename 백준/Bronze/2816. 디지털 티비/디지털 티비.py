
n = int(input())

arr = []

for i in range(n):
    name = input()
    arr.append(name)

cur = 0
ans = []

while arr[cur] != 'KBS1':
    cur += 1
    ans.append(1)

for _ in range(cur):
    ans.append(4)

cur = 0

arr.remove('KBS1')

arr=['KBS1'] + arr

while arr[cur] != 'KBS2':
    cur += 1
    ans.append(1)

for _ in range(cur-1):
    ans.append(4)

for i in ans:
    print(i,end='')