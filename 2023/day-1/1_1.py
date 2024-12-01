def solve(s: str):
    # let a be first and b be last then a*10+b
    a = -1
    b = -1
    for ch in s:
        if ch.isdigit():
            if a == -1:
                a = int(ch)
            b = int(ch)
    return a*10+b
    #print(a*10+b)

ans = 0
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        if (line):
            ans += solve(line)
print(ans)
