from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    test_dict = defaultdict(int)
    count_dict = defaultdict(list)

    for i in arr:
        test_dict[i] += 1

    lst = []

    for x in arr:
        if test_dict[x] >= 6:
            lst.append(x)

    for cnt, team in enumerate(lst):
        cnt += 1

        count_dict[team].append(cnt)

    sorted_dict = sorted(count_dict, key = lambda x: (sum(count_dict[x][:4]), count_dict[x][4]))
    print(sorted_dict[0])