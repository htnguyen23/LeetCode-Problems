class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # ATTEMPT 2

        # helper function
        def dfs(row, col):
            if (row < 0) or (row >= m) or (col < 0) or (col >= n) or (grid[row][col] == '0'):
                return
            grid[row][col] = '0' # mark the cell as visited
            # explore neighboring land cells
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        m, n = len(grid), len(grid[0])
        islands = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    islands += 1
                    # start DFS traversal for the current island
                    dfs(row, col)

        return islands

        # # ATTEMPT 1
        # # find [i][j] = "1" where [i-1][j],
        # #                         [i][j-1],
        # #                         [i][j+1],
        # #                         [i+1][j] are = "0"
        # # if any of ^^ = "1", then those corresponding neighbors need to = "0" -> use stack to check for island criteria
        # # if any i or j < 0 or > n, then it = "0"

        # m, n = len(grid), len(grid[0])
        
        # # each island gets it's own stack?
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "1"
