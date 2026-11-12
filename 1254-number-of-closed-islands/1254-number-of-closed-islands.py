class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] != 0:
                    continue

                stack = [(y, x)]
                grid[y][x] = 1
                closed = True

                while stack:
                    cy, cx = stack.pop()

                    if cy == 0 or cx == 0 or cy == rows-1 or cx == cols-1:
                        closed = False

                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx

                        if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == 0:
                            grid[ny][nx] = 1
                            stack.append((ny, nx))

                if closed:
                    islands += 1

        return islands