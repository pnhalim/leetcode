class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1 for col in range(n)] for row in range(m)]
        
        for col in range(1, n):
            for row in range(1, m):
                memo[row][col] = memo[row-1][col] + memo[row][col-1]
                
        return memo[m-1][n-1]