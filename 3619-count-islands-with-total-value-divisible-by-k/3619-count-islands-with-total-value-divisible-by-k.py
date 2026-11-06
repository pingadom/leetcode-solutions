class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        islands = []
        real = []
        seen = set()
        for y in range(0,len(grid)):
            for x in range(0,len(grid[0])):
                if (y,x) in seen:
                    continue
                else:
                    seen.add((y,x))
                if grid[y][x] > 0:
                    islands.append(grid[y][x]+int(self.recurse(grid,y,x,seen)))
   
        c = 0
        for item in islands:
            if (item%k == 0):
                c+=1

        return c

    def recurse(self, grid: List[List[int]],y,x,seen):
        left,right,up,down = 0,0,0,0
        if x+1 < (len(grid[0])):
            if (grid[y][x+1] > 0) and (y,x+1) not in seen:
                seen.add((y,x+1))
                right = grid[y][x+1] + self.recurse(grid,y,x+1,seen)
        if y+1 < (len(grid)):    
            if (grid[y+1][x] > 0) and (y+1,x) not in seen:
                seen.add((y+1,x))
                down = grid[y+1][x] + self.recurse(grid,y+1,x,seen)
        if x-1 >= 0:
            if (grid[y][x-1] > 0) and (y,x-1) not in seen:
                seen.add((y,x-1))
                left = grid[y][x-1] + self.recurse(grid,y,x-1,seen)
        if y-1 >= 0:    
            if (grid[y-1][x] > 0) and (y-1,x) not in seen:
                seen.add((y-1,x))
                up = grid[y-1][x] + self.recurse(grid,y-1,x,seen)   
        return left+right+up+down

        



        