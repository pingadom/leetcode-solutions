class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m,n = len(grid[0]), len(grid)  
        seen_server = set()
        seen_row = {}
        seen_col = {}

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i not in seen_row:
                        seen_row[i] = []
                    if j not in seen_col:
                        seen_col[j] = []
                    seen_row[i].append((i,j))
                    seen_col[j].append((i,j))
        
        for item in list(seen_row.values()):
            if len(item) > 1:
                for v in item:
                    seen_server.add(v)
        
        for item in list(seen_col.values()):
            if len(item) > 1:
                for v in item:
                    seen_server.add(v)
        
        return len(seen_server)
        

