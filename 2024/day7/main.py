import math

filename = "in.txt"

with open(filename) as f:
    lines = [line.strip() for line in f]
    sum = 0
    for line in lines:
        line = line.split(": ")
        target = int(line[0])
        eq = list(map(int, line[1].split(" ")))

        def evaluate(s, l):
            cur = 0
            if s[0] == "+":
                cur = l[0] + l[1]
            else:
                cur = l[0] * l[1]
            for i in range(1, len(s)):
                if s[i] == "+":
                    cur += l[i + 1]
                else:
                    cur *= l[i + 1]
            return cur

        def generate_combinations(n, s, l):
            if n == 0:
                return evaluate(s, l) == target
            ret = False
            for ch in "+*":
                s.append(ch)
                ret |= generate_combinations(n - 1, s, eq)
                del s[-1]
            return ret

        if generate_combinations(len(eq) - 1, [], eq):
            sum += target
    print(sum)

with open(filename) as f:
    lines = [line.strip() for line in f]
    sum = 0
    for line in lines:
        line = line.split(": ")
        target = int(line[0])
        eq = list(map(int, line[1].split(" ")))

        def evaluate(s, l):
            cur = 0
            if s[0] == "+":
                cur = l[0] + l[1]
            elif s[0] == "*":
                cur = l[0] * l[1]
            else:
                cur = (10 ** (int(math.log10(l[1]) + 1))) * l[0] + l[1]

            for i in range(1, len(s)):
                if s[i] == "+":
                    cur += l[i + 1]
                elif s[i] == "*":
                    cur *= l[i + 1]
                else:
                    cur = (10 ** (int(math.log10(l[i + 1]) + 1))) * cur + l[i + 1]
            return cur

        def generate_combinations(n, s, l):
            if n == 0:
                return evaluate(s, l) == target
            ret = False
            for ch in "+*|":
                s.append(ch)
                ret |= generate_combinations(n - 1, s, eq)
                del s[-1]
            return ret

        if generate_combinations(len(eq) - 1, [], eq):
            sum += target
    print(sum)
