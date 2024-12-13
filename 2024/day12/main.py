filename = "in.txt"
with open(filename) as f:
    grid = [list(line.strip()) for line in f]
    grid = {
        i + 1j * j: int(c) if c.isdigit() else c
        for i, row in enumerate(grid)
        for j, c in enumerate(row)
    }

    vis = set()
    l = set()

    def dfs(src):
        ch = grid.get(src)
        ans = 1
        l.add(src)
        for k in range(4):
            new_src = src + 1j**k
            new_val = grid.get(new_src)
            if new_val == ch:
                if new_src not in vis:
                    vis.add(new_src)
                    ans += dfs(new_src)
        return ans

    d = {}
    ans = 0
    for x in grid:
        if x not in vis:
            vis.add(x)
            cnt = dfs(x)
            fences = 0
            for c in l:
                for k in range(4):
                    if c + 1j**k not in l:
                        fences += 1
            ans += fences * cnt
        l = set()
    print("Part 1:", ans)

with open(filename) as f:
    grid = [list(line.strip()) for line in f]
    grid = {
        i + 1j * j: int(c) if c.isdigit() else c
        for i, row in enumerate(grid)
        for j, c in enumerate(row)
    }

    vis = set()
    l = set()

    def dfs(src):
        ch = grid.get(src)
        ans = 1
        l.add(src)
        for k in range(4):
            new_src = src + 1j**k
            new_val = grid.get(new_src)
            if new_val == ch:
                if new_src not in vis:
                    vis.add(new_src)
                    ans += dfs(new_src)
        return ans

    d = {}
    ans = 0
    for x in grid:
        if x not in vis:
            vis.add(x)
            cnt = dfs(x)
            fences = []
            print(grid.get(x))
            print([(x.real, x.imag) for x in l])
            # break
        l = set()

    # print("Part 2:", ans)
