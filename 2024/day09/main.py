from collections import defaultdict

filename = "in.txt"


def computeChecksum(disk):
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == ".":
            continue
        checksum += i * disk[i]
    return checksum


with open(filename) as f:
    s = f.read().strip()
    flag = True
    disk = []
    cnt = 0
    for ch in s:
        if flag:
            disk.extend([cnt] * int(ch))
            cnt += 1
            flag = False
        else:
            disk.extend(list("." * (int(ch))))
            flag = True

    j = len(disk) - 1
    for i in range(len(disk)):
        if i > j:
            break

        if disk[i] == ".":
            disk[i], disk[j] = disk[j], disk[i]
            while disk[j] == ".":
                j -= 1

    print(computeChecksum(disk))

with open(filename) as f:
    s = f.read().strip()
    flag = True
    disk = []
    cnt = 0
    cnt_tracker = []
    for ch in s:
        if flag:
            disk.extend([cnt] * int(ch))
            cnt_tracker.append([cnt, int(ch)])
            cnt += 1
            flag = False
        else:
            disk.extend(list("." * (int(ch))))
            cnt_tracker.append([".", int(ch)])
            flag = True

    i = 0
    j = len(cnt_tracker) - 1
    while j >= 0:
        while cnt_tracker[j][0] == ".":
            j -= 1
        for i in range(j):
            if cnt_tracker[i][0] == "." and cnt_tracker[i][1] >= cnt_tracker[j][1]:
                diff = cnt_tracker[i][1] - cnt_tracker[j][1]

                cnt_tracker[i][0] = cnt_tracker[j][0]
                cnt_tracker[i][1] = cnt_tracker[j][1]

                cnt_tracker[j][0] = "."
                cnt_tracker.insert(i + 1, [".", diff])
                break
        j -= 1
    disk = []
    for val in cnt_tracker:
        disk.extend([val[0]] * val[1])
    print(computeChecksum(disk))
