n = int(input())
exist = []

for _ in range(n):
    words = list(map(str, input().split()))
    flag = 0
    for i in range(len(words)):
        if words[i][0].upper() not in exist:
            exist.append(words[i][0].upper())
            flag = 1
            words[i] = '[' + words[i][0] + ']' + words[i][1:]
            print(' '.join(words))
            break

    if not flag:
        for i in range(len(words)):
            check = 0
            for j in range(len(words[i])):
                if words[i][j].upper() not in exist:
                    exist.append(words[i][j].upper())
                    flag = 1
                    check = 1
                    words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j+1:]

                    print(' '.join(words))
                    break

            if check: break
        if not flag:
            print(' '.join(words))



