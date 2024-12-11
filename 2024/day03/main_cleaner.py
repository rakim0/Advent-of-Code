def solve(input):
    ans = 0
    n = len(input)
    i = 0
    while i < n:
        if input[i:].startswith("mul("):
            j = input.find(")", i)
            check = input[i + 4 : j]
            if (
                all(map(lambda x: x.isdigit() or x == ",", check))
                and check.count(",") == 1
                and not check[0] == ","
            ):
                a, b = map(int, check.split(","))
                ans += a * b
            i += 4
        i += 1
    return ans


def solve2(input):
    ans = 0
    n = len(input)
    i = 0
    flag = True
    while i < n:
        if input[i:].startswith("do()"):
            flag = True

        elif input[i:].startswith("don't()"):
            flag = False

        elif input[i:].startswith("mul("):
            j = input.find(")", i)
            check = input[i + 4 : j]
            if (
                all(map(lambda x: x.isdigit() or x == ",", check))
                and check.count(",") == 1
                and not check[0] == ","
                and flag
            ):
                a, b = map(int, check.split(","))
                ans += a * b

        i += 1

    return ans


with open("in.txt") as f:
    data = f.read()
    print(solve(data))
    print(solve2(data))
