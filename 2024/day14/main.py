"""
So for today's problem we don't really need grids
we can simulate and calculate the final destination 

initial location: x,  y
speed           : vx, vy

so at each step it's newx = x+vx and newy = y+vy
and it teleports to other side? 
does this mean that it's just mod?

let's check with the example
p = 2,4
v = 2,-3

(2,4) -> (4, 1) -> (6, -2) = (6, 7)

so I can just add and mod yeah?
(a%mod + b%mod) % mod = (a+b) % mod

since there are 100 steps, then just (a+100*b) % mod

after that need to check which quadrant it lies in.
And middle rows/columns wouldn't be considered 

m = number of rows
n = number of columns

so just check if it's greater or less than m/2 and n/2
and accordingly add for each quandrant
"""

import sys

with open("in.txt") as f:
    m = 101
    n = 103
    count = [[0, 0], [0, 0]]
    for line in f.readlines():
        p, v = line.strip().split(" ")
        px, py = list(map(int, p[2:].split(",")))
        vx, vy = list(map(int, v[2:].split(",")))
        py = n - py - 1
        vy *= -1
        fx = (px + (100 * vx) + m) % m
        fy = (py + (100 * vy) + n) % n
        if fx != m // 2 and fy != n // 2:
            count[fx > m / 2][fy > n / 2] += 1
    print(count[0][0] * count[0][1] * count[1][0] * count[1][1])


with open("in.txt") as f:
    m = 101
    n = 103
    lines = [line.strip() for line in f.readlines()]

    def checkGrid(grid):
        for x in range(0, m):
            cnt = 0
            for y in range(0, n):
                if grid[y][x] == "#":
                    cnt += 1
                else:
                    cnt = 0
                if cnt > 20:
                    return True
        return False

    while True:
        for i in range(0, 100000):
            grid = [["." for _ in range(m)] for _ in range(n)]
            for line in lines:
                p, v = line.strip().split(" ")
                px, py = list(map(int, p[2:].split(",")))
                vx, vy = list(map(int, v[2:].split(",")))
                py = n - py - 1
                vy *= -1
                fx = (px + (i * vx) + m) % m
                fy = (py + (i * vy) + n) % n
                if fx != m // 2 and fy != n // 2:
                    count[fx > m / 2][fy > n / 2] += 1
                grid[fy][fx] = "#"
            if checkGrid(grid):
                grid = grid[-1::-1]
                for row in grid:
                    print("".join(row))
                    sys.stdout.flush()
                print(i)
                ch = input()
                if ch == "q":
                    sys.exit()
