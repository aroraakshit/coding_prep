class Solution: # 40ms, faster than 97% solutions
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        leftView = [max(row) for row in grid]
        topView = [max([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0]))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                ans += min(topView[j], leftView[i]) - grid[i][j]
        return ans