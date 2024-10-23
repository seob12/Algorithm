s = list(map(str, input()))

t = s[::-1]

word = ''
wor = ''

for i in s:
    word += i

for j in t:
    wor += j


if word==wor:
    print(1)
else:
    print(0)