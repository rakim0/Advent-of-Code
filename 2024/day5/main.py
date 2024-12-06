"""
5   00:12:12  1906      0   00:25:16  2327      0
"""

from collections import defaultdict

with open("in.txt") as f:
    lines = [line.strip() for line in f]
    order = defaultdict(list)
    ans = 0
    for line in lines:
        if "|" in line:
            a, b = list(map(int, line.split("|")))
            order[a].append(b)
        elif "," in line:
            l = list(map(int, line.split(",")))
            n = len(l)
            i = n - 1

            flag = True
            while i - 1 >= 0:
                if l[i] not in order[l[i - 1]] or l[i - 1] in order[l[i]]:
                    flag = False
                    break
                i -= 1

            if flag:
                ans += l[n // 2]
    print(ans)

with open("in.txt") as f:
    lines = [line.strip() for line in f]
    order = defaultdict(list)
    ans = 0
    for line in lines:
        if "|" in line:
            a, b = list(map(int, line.split("|")))
            order[a].append(b)
        elif "," in line:
            l = list(map(int, line.split(",")))
            n = len(l)
            i = n - 1

            flag = True
            while i - 1 >= 0:
                if l[i] not in order[l[i - 1]] or l[i - 1] in order[l[i]]:
                    flag = False
                    break
                i -= 1

            if not flag:
                newFlag = True
                while newFlag:
                    newFlag = False
                    i = n - 1
                    while i - 1 >= 0:
                        if l[i - 1] in order[l[i]]:
                            l[i], l[i - 1] = l[i - 1], l[i]
                            newFlag = True
                        i -= 1
                ans += l[n // 2]
    print(ans)
