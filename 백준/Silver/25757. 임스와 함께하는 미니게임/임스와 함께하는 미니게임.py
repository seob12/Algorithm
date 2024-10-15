n,y = map(str, input().split())
ans = 0
game = set()


for _ in range(int(n)):
    name = input()
    game.add(name)



if y == 'Y':
    ans = len(game)
elif y == 'F':
    ans = len(game) // 2
else:
    ans = len(game) // 3

print(ans)