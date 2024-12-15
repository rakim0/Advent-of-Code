import sys

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
    for row in grid:
        print("".join(row))
    print()
    print("Part 1: ", ans)
