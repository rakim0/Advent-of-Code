with open("int.txt") as f:
    keys = []
    locks = []
    key = [0] * 5
    pos = 0
    lock = False
    for line in f.readlines():
        str = list(line.strip())
        if str == []:
            if lock:
                locks.append(key)
            else:
                keys.append(key)
            key = [0] * 5
            lock = False
            pos = -1

        elif str == ["#"] * 5 and pos == 0:
            lock = True

        elif str == ["#"] * 5 and pos == 6:
            lock = False
        else:
            key = [
                sum(x) for x in zip(key, list(map(lambda c: 1 if c == "#" else 0, str)))
            ]
        pos += 1
    if key != [0] * 5:
        keys.append(key)

    ans = 0
    for key in keys:
        for lock in locks:
            joined = [sum(x) for x in zip(key, lock)]
            if all(map(lambda x: x <= 5, joined)):
                ans += 1
    print(ans)
