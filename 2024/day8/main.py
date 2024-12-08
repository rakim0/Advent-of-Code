from collections import defaultdict

filename = "in.txt"

with open(filename) as f:
    grid = [list(line.strip()) for line in f]
    m = len(grid)
    n = len(grid[0])
    d = defaultdict(list)

    for i in range(m):
        for j in range(n):
            if grid[i][j] != ".":
                d[grid[i][j]].append([i, j])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def check(x, y):
        if x >= 0 and x < m and y >= 0 and y < n:
            return True
        else:
            return False

    cnt = 0
    s = set()
    for values in list(d.values()):
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                if i == j:
                    continue
                dx = values[i][0] - values[j][0]
                dy = values[i][1] - values[j][1]

                nx = values[i][0] + dx
                ny = values[i][1] + dy
                if check(nx, ny):
                    s.add((nx, ny))
                    cnt += 1
                nx = values[j][0] - dx
                ny = values[j][1] - dy
                if check(nx, ny):
                    s.add((nx, ny))
                    cnt += 1
    print(len(s))


def printGrid(grid):
    for line in grid:
        print(line)


with open(filename) as f:
    grid = [list(line.strip()) for line in f]
    m = len(grid)
    n = len(grid[0])
    d = defaultdict(list)

    for i in range(m):
        for j in range(n):
            if grid[i][j] != ".":
                d[grid[i][j]].append([i, j])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def check(x, y):
        if x >= 0 and x < m and y >= 0 and y < n:
            return True
        else:
            return False

    cnt = 0
    s = set()

    for values in list(d.values()):
        l = []
        if len(values) == 1:
            continue
        for i in range(len(values)):
            s.add((values[i][0], values[i][1]))
            grid[values[i][0]][values[i][1]] = "#"
            for j in range(0, len(values)):
                if i == j:
                    continue
                dx = values[i][0] - values[j][0]
                dy = values[i][1] - values[j][1]
                nx = values[i][0] + dx
                ny = values[i][1] + dy

                while check(nx, ny):
                    s.add((nx, ny))
                    grid[nx][ny] = "#"
                    cnt += 1
                    nx += dx
                    ny += dy

                nx = values[j][0] - dx
                ny = values[j][1] - dy
                while check(nx, ny):
                    s.add((nx, ny))
                    grid[nx][ny] = "#"
                    cnt += 1
                    nx -= dx
                    ny -= dy

    printGrid(grid)
    print(len(s))
