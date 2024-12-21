def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()


with open("in.txt") as f:
    grid = []
    moves = []
    flag = False
    for line in f:
        line = line.strip()
        if line == "":
            flag = True
        else:
            if not flag:
                grid.append(list(line))
            else:
                moves.extend(list(line))
    x, y = 0, 0
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "@":
                x, y = i, j
                break
        if grid[x][y] == "@":
            break

    map_moves = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

    def push(x, y, m):
        newx = x + m[0]
        newy = y + m[1]
        if 0 <= x < n or 0 <= y < m:
            if grid[newx][newy] != "#":
                if grid[newx][newy] != ".":
                    push(newx, newy, m)
                if grid[newx][newy] == ".":
                    grid[x][y], grid[newx][newy] = grid[newx][newy], grid[x][y]
                    x, y = newx, newy
        return (x, y)

    for move in moves:
        new_coordinates = push(x, y, map_moves[move])
        if new_coordinates:
            x, y = new_coordinates

    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "O":
                ans += 100 * i + j

    print("Part 1: ", ans)

"""
for part 2 

while pushing up, check if it's possible 
to push each half of box before committing it

I think recursive will be easy but let's see.

to check if it's possible, then at the end it should have a '.'
"""
with open("int.txt") as f:
    grid = []
    moves = []
    flag = False
    double = {"@": "@.", "#": "##", "O": "[]", ".": ".."}
    for line in f:
        line = line.strip()
        if line == "":
            flag = True
        else:
            if not flag:
                tl = []
                for x in line:
                    tl.extend(list(double[x]))
                grid.append(tl)
            else:
                moves.extend(list(line))
    x, y = 0, 0
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "@":
                x, y = i, j
                break
        if grid[x][y] == "@":
            break

    map_moves = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

    def push2(x, y, m):
        newx = x + m[0]
        newy = y + m[1]
        return (x, y)

    def push_possible(x, y, m):
        newx = x + m[0]
        if grid[newx][y] == ".":
            return newx
        elif grid[newx][y] == "#":
            return x
        return push_possible(newx, y, m)

    def push(x, y, m):
        newx = x + m[0]
        newy = y + m[1]
        if 0 <= x < n or 0 <= y < m:
            if grid[newx][newy] != "#":
                if grid[newx][newy] != ".":
                    push(newx, newy, m)
                if grid[newx][newy] == ".":
                    grid[x][y], grid[newx][newy] = grid[newx][newy], grid[x][y]
                    x, y = newx, newy
        return (x, y)

    def push(x, y, m):
        newx = x + m[0]
        newy = y + m[1]
        if 0 <= x < n or 0 <= y < m:
            if grid[newx][newy] != "#":
                if grid[newx][newy] != ".":
                    push(newx, newy, m)
                if grid[newx][newy] == ".":
                    grid[x][y], grid[newx][newy] = grid[newx][newy], grid[x][y]
                    x, y = newx, newy
        return (x, y)

    def push2(x, y, m):
        newx = x + m[0]
        newy = y + m[1]
        if 0 <= x < n or 0 <= y < m:
            if grid[newx][newy] != "#":
                if grid[newx][newy] != ".":
                    push2(newx, newy, m)
                if grid[newx][newy] == ".":
                    if grid[x][y] == "]":
                        y -= 1
                    if grid[x][y] == "[":
                        if (x, y + 1) != push2(x, y + 1, m):
                            grid[x][y], grid[newx][newy] = grid[newx][newy], grid[x][y]
                    else:
                        grid[x][y], grid[newx][newy] = grid[newx][newy], grid[x][y]
                    x, y = newx, newy
        return (x, y)

    def check(x, y):
        return 0 <= x < n or 0 <= y < m

    for move in moves:
        if move in "<>":
            new_coordinates = push(x, y, map_moves[move])
        else:
            new_coordinates = push2(x, y, map_moves[move])
        if new_coordinates:
            x, y = new_coordinates
        print_grid(grid)

    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "[":
                ans += 100 * i + j

    print("Part 2: ", ans)
