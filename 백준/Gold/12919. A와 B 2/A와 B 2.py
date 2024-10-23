s = input()
t = input()

ans = 0

def backtracking(target):
    global ans

    if len(s) == len(target):
        if s == target:
            ans = 1
        return

    if target[-1] == 'A':
        backtracking(target[:-1])

    if target[0] == 'B':
        backtracking(target[::-1][:-1])



backtracking(t)
print(ans)