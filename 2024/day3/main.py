import re
pattern = r'mul\((\d+),(\d+)\)'
with open('in.txt') as f:
    lines = [line.strip() for line in f]
    ans = 0
    p = r'\d+'
    for line in lines:
        for match in re.finditer(pattern, line):
            m = match.groups()
            ans += int(m[0])*int(m[1])
        
    print(ans)

# part 2
pattern = r'do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)'
with open('in.txt') as f:
    lines = [line.strip() for line in f]
    ans = 0
    p = r'\d+'
    flag = True
    for line in lines:
        for match in re.finditer(pattern, line):
            if (match.group() == "don't()"):
                flag = False
            elif match.group() == "do()":
                flag = True
            else:
                if flag:
                    m = match.groups()
                    ans += int(m[0])*int(m[1])
        
    print(ans)