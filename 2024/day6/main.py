import copy


directions = {}
directions["^"] = (-1, 0)
directions["v"] = (1, 0)
directions[">"] = (0, 1)
directions["<"] = (0, -1)

next_transformation = {}
next_transformation["^"] = ">"
next_transformation[">"] = "v"
next_transformation["v"] = "<"
next_transformation["<"] = "^"

visited = list()
total = 0
with open("in.txt") as f:
    ans = 0
    grid = [list(line.strip()) for line in f]

    x, y = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                x = i
                y = j
                break

    def check_xy():
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

    cur = grid[x][y]
    t = 0

    while check_xy():
        alreadyX = 0
        cnt = 0
        while check_xy() and grid[x][y] != "#":
            grid[x][y] = "X"
            visited.append([x, y])
            x += directions[cur][0]
            y += directions[cur][1]
        if check_xy() and grid[x][y] == "#":
            x -= directions[cur][0]
            y -= directions[cur][1]
        if check_xy():
            cur = next_transformation[cur]
    total = sum([line.count("X") for line in grid])
    print(total + 1)

with open("in.txt") as f:
    ans = 0
    grid = [list(line.strip()) for line in f]

    def check_xy(x, y, grid):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

    def printGrid(grid):
        for line in grid:
            print(line)

    def checkloop(grid):
        x, y = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "^":
                    x = i
                    y = j
                    break

        cur = grid[x][y]
        cnt = total
        while check_xy(x, y, grid):
            while check_xy(x, y, grid) and grid[x][y] != "#":
                grid[x][y] = "X"
                x += directions[cur][0]
                y += directions[cur][1]
            if check_xy(x, y, grid) and grid[x][y] == "#":
                x -= directions[cur][0]
                y -= directions[cur][1]
            if check_xy(x, y, grid):
                cur = next_transformation[cur]
            cnt -= 1
            if cnt <= 0:
                return True
        return False

    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ".":
                grid[i][j] = "#"
                copy_grid = copy.deepcopy(grid)
                if [i, j] in visited:
                    if checkloop(copy_grid):
                        ans += 1
                grid[i][j] = "."
    print(ans)
