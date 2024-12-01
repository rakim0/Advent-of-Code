def preprocess(s: str):
    d = {"one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    words = d.keys()
    news = ""
    for i in range(len(s)):
         if (s[i].isdigit()):
             news += s[i]
         if (i+3 <= len(s) and s[i:i+3] in words):
             news += d[s[i:i+3]]

         if (i+4 <= len(s) and s[i:i+4] in words):
             news += d[s[i:i+4]]

         if (i+5 <= len(s) and s[i:i+5] in words):
             news += d[s[i:i+5]]
    return news

def solve(s: str):
    # let a be first and b be last then a*10+b
    s = preprocess(s)
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
