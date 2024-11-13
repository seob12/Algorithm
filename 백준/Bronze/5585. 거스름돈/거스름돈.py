n = int(input())

change = 1000-n
ans = 0

while 1:
    if change >= 500:
        ans += change // 500
        change %= 500
    elif change >= 100:
        ans += change // 100
        change %= 100
    elif change >= 50:
        ans += change // 50
        change %= 50
    elif change >= 10:
        ans += change // 10
        change %= 10
    elif change >= 5:
        ans += change // 5
        change %= 5
    else:
        ans += change
        break


print(ans)