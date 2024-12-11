# part 1
def part1():
    with open("in.txt") as f:
        ans = 0
        lines = [line.strip() for line in f]
        # horizontal
        for line in lines:
            ans += line.count("XMAS")
            ans += line.count("SAMX")

        # vertical
        for i in range(len(lines[0])):
            temp = ""
            for j in range(len(lines)):
                temp += lines[j][i]
            ans += temp.count("XMAS")
            ans += temp.count("SAMX")

        # diagonal

        n = len(lines)
        m = len(lines[0])

        for i in range(n):
            for j in range(m):
                if lines[i][j] == "X" and (i < n and j < m):
                    # search down and right
                    x = i
                    y = j
                    word = ""
                    for d in range(4):
                        if x + d >= n or y + d >= m:
                            break
                        word += lines[x + d][y + d]
                        if word == "XMAS":
                            ans += 1
                    # search up and left
                    x = i
                    y = j
                    word = ""
                    for d in range(4):
                        if x - d < 0 or y - d < 0:
                            break
                        word += lines[x - d][y - d]
                        if word == "XMAS":
                            ans += 1
                    # search down and left
                    x = i
                    y = j
                    word = ""
                    for d in range(4):
                        if x + d >= n or y - d < 0:
                            break
                        word += lines[x + d][y - d]
                        if word == "XMAS":
                            ans += 1
                    # search up and right
                    x = i
                    y = j
                    word = ""
                    for d in range(4):
                        if x - d < 0 or y + d >= m:
                            break
                        word += lines[x - d][y + d]
                        if word == "XMAS":
                            ans += 1
        print(ans)


# part 2
def part2():
    with open("in.txt") as f:
        ans = 0
        lines = [line.strip() for line in f]
        n = len(lines)
        m = len(lines[0])
        for i in range(n):
            for j in range(m):
                if (
                    lines[i][j] == "A"
                    and i + 1 < n
                    and i - 1 >= 0
                    and j + 1 < m
                    and j - 1 >= 0
                ):
                    temps = sorted(
                        lines[i - 1][j - 1] + lines[i][j] + lines[i + 1][j + 1]
                    )
                    temps2 = sorted(
                        lines[i - 1][j + 1] + lines[i][j] + lines[i + 1][j - 1]
                    )
                    if temps == temps2 == ["A", "M", "S"]:
                        ans += 1
        print(ans)


part1()
part2()
# import time

# t1 = time.time_ns()
# for i in range(times := 1000):
#     part1()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")
# t1 = time.time_ns()
# for i in range(times := 1000):
#     part2()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")
