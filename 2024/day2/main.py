def check(d):
    inc = (d[0] < d[1])
    dec = (d[1] < d[0])
    for i in range(len(d)-1):
        if (inc and (d[i] > d[i+1])):
            return False
        if (dec and d[i+1] > d[i]):
            return False
    for i in range(len(d)-1):
        diff = abs(d[i]-d[i+1])
        if (diff < 1 or diff > 3):
            return False
    return True

def check2(d):
    if (check(d)):
        return True
    print(d)
    for i in range(0,len(d)):
        ld = d.copy()
        del ld[i]
        if (check(ld)):
            return True
    return False

with open('in.txt') as f:
    lines = [line.strip() for line in f]
    ans = 0
    for line in lines:
        d = [int(x) for x in line.split()]
        if (check(d)):
            ans += 1
    print(ans)
        
with open('in.txt') as f:
    lines = [line.strip() for line in f]
    ans = 0
    for line in lines:
        d = [int(x) for x in line.split()]
        if (check2(d)):
            ans += 1
    print(ans)