import re
from functools import cache
import sympy as sym

with open("in.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    i = 0
    pattern = r"(X\+([0-9]*))|(Y\+([0-9]*))"
    target_pattern = r"(X\=([0-9]*))|(Y\=([0-9]*))"

    def getXY(line):
        match = re.findall(pattern, line)
        return (match[0][1], match[1][3])

    def getTarget(line):
        match = re.findall(target_pattern, line)
        return (match[0][1], match[1][3])

    l = []

    while i + 2 < len(lines):
        a = list(map(int, getXY(lines[i])))
        b = list(map(int, getXY(lines[i + 1])))
        t = list(map(int, getTarget(lines[i + 2])))

        @cache
        def getPos(x, y, acnt, bcnt):
            if x > t[0] or y > t[1] or acnt >= 100 or bcnt >= 100:
                return 500
            if x == t[0] and y == t[1]:
                return 0

            ans = 500
            ans = min(3 + getPos(x + a[0], y + a[1], acnt + 1, bcnt), ans)
            ans = min(1 + getPos(x + b[0], y + b[1], acnt, bcnt + 1), ans)
            return ans

        ans = getPos(0, 0, 0, 0)
        if ans < 500:
            l.append(ans)

        i += 4
    print(sum(l))


with open("in.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    i = 0
    pattern = r"(X\+([0-9]*))|(Y\+([0-9]*))"
    target_pattern = r"(X\=([0-9]*))|(Y\=([0-9]*))"

    def getXY(line):
        match = re.findall(pattern, line)
        return (match[0][1], match[1][3])

    def getTarget(line):
        match = re.findall(target_pattern, line)
        return (match[0][1], match[1][3])

    sum = 0

    while i + 2 < len(lines):
        a = list(map(int, getXY(lines[i])))
        b = list(map(int, getXY(lines[i + 1])))
        t = list(map(int, getTarget(lines[i + 2])))
        t[0] += 10000000000000
        t[1] += 10000000000000

        x, y = sym.symbols("x,y")
        eq1 = sym.Eq(a[0] * x + b[0] * y, t[0])
        eq2 = sym.Eq(a[1] * x + b[1] * y, t[1])
        result = sym.solve([eq1, eq2], [x, y])
        if result[x].is_integer and result[y].is_integer:
            # print(a, b, t)
            sum += result[x] * 3 + result[y] * 1
        i += 4
    print(sum)
