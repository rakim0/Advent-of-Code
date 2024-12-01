import collections
# part 1
with open('test.txt') as f:
    l = []
    r = []
    for line in f.readlines():
        nl, nr = map(int, line.split())
        l.append(nl)
        r.append(nr)
    ans = 0
    l.sort()
    r.sort()
    for a, b in zip(l, r):
        ans += abs(a-b)
    print(ans)

# part 2
with open('test.txt') as f:
    l = []
    r = []
    for line in f.readlines():
        nl, nr = map(int, line.split())
        l.append(nl)
        r.append(nr)
    r = collections.Counter(r)
    ans = sum(l*r[l] for l in l)
    print(ans)
