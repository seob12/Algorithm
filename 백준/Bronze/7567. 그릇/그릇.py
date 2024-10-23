k = input()
n = len(k)

result = 10

for i in range(n-1):
    if k[i] == k[i+1]:
        result += 5
    else:
        result += 10

print(result)