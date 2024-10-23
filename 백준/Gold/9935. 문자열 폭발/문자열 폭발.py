s = input()
bomb = input()
arr = []

for i in range(len(s)):
    arr.append(s[i])
    if s[i] == arr[-1] and ''.join(arr[-len(bomb):]) == bomb:
        del arr[-len(bomb):]
        
s = ''.join(arr)

if len(s) == 0:
    print('FRULA')
else:
    print(s)





