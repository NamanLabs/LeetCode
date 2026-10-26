class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        valid_islands = 0
        
        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            
            val = grid[r][c]
            grid[r][c] = 0 
            
            val += dfs(r + 1, c)
            val += dfs(r - 1, c)
            val += dfs(r, c + 1)
            val += dfs(r, c - 1)
            
            return val
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] > 0:
                    if dfs(r, c) % k == 0:
                        valid_islands += 1
                        
        return valid_islands
