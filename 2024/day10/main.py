from collections import defaultdict

filename = "in.txt"

with open(filename) as f:
    grid = [list(line.strip()) for line in f]
    grid = {
        i + 1j * j: int(c) if c.isdigit() else c
        for i, row in enumerate(grid)
        for j, c in enumerate(row)
    }

    def dfs(cur, grid, visited):
        x = grid.get(cur)

        if x == 9:
            visited.add(cur)

        ans = 0
        for k in range(4):
            newx = cur + 1j**k
            newVal = grid.get(newx)
            if newVal and newVal != "." and newVal - x == 1:
                ans += dfs(newx, grid, visited)
        return ans

    ans = 0
    for co in grid.keys():
        if grid.get(co) == 0:
            visited = set()
            dfs(co, grid, visited)
            ans += len(visited)
    print(ans)

with open(filename) as f:
    grid = [list(line.strip()) for line in f]
    grid = {
        i + 1j * j: int(c) if c.isdigit() else c
        for i, row in enumerate(grid)
        for j, c in enumerate(row)
    }

    def dfs(cur, grid):
        x = grid.get(cur)

        if x == 9:
            return 1

        ans = 0
        for k in range(4):
            newx = cur + 1j**k
            newVal = grid.get(newx)
            if newVal and newVal != "." and newVal - x == 1:
                ans += dfs(newx, grid)
        return ans

    ans = 0
    for co in grid.keys():
        if grid.get(co) == 0:
            ans += dfs(co, grid)
    print(ans)
