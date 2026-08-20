class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            for nr, nc in directions:
                dfs(r + nr, c + nc)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands





























        # islands = 0
        # ROWS, COLS = len(grid), len(grid[0])
        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] #directions

        # def dfs(r, c):
        #     if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
        #         return
            
        #     grid[r][c] = "0"
        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc)



        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == "1":
        #             dfs(r, c)
        #             islands += 1

        # return islands




        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # directions
        # ROWS, COLS = len(grid), len(grid[0])
        # islands = 0

        # def bfs(r, c):
        #     q = deque()
        #     grid[r][c] = "0"
        #     q.append((r, c))

        #     while q:
        #         row, col = q.popleft()
        #         for dr, dc in directions:
        #             nr, nc = row + dr, col + dc
        #             if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0"):
        #                 continue
                    
        #             q.append((nr,nc))
        #             grid[nr][nc] = "0"

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == "1":
        #             bfs(r, c)
        #             islands += 1

        # return islands