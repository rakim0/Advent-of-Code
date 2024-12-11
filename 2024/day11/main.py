from math import log, ceil
from functools import cache


def count_digit(n):
    cnt = 0
    while n > 0:
        n //= 10
        cnt += 1
    return cnt


def get_half(n):
    l = count_digit(n)
    left = 0
    for i in range(l // 2):
        left += (n % 10) * (10**i)
        n //= 10
    right = 0
    for i in range(l // 2):
        right += (n % 10) * (10**i)
        n //= 10
    return (left, right)


l = [3279, 998884, 1832781, 517, 8, 18864, 28, 0]
iter = 25
for _ in range(1, iter + 1):
    n = len(l)
    i = 0
    newVal = []
    while i < n:
        x = l[i]
        if x == 0:
            l[i] = 1
        elif count_digit(x) % 2 == 0:
            t = get_half(x)
            l[i] = t[0]
            newVal.append(t[1])
            # l.insert(i, t[1])
        else:
            l[i] *= 2024
        i += 1
    l.extend(newVal)
    iter -= 1

print("Part 1:", len(l))


# ans will return the count of numbers being generated
@cache
def ans(x, n):
    if n == 0:
        return 1
    if x == 0:
        return ans(1, n - 1)

    if count_digit(x) % 2 == 0:
        t = get_half(x)
        return ans(t[1], n - 1) + ans(t[0], n - 1)

    return ans(x * 2024, n - 1)


l = [3279, 998884, 1832781, 517, 8, 18864, 28, 0]
iter = 75
print("Part 2:", sum([ans(i, iter) for i in l]))
