class Solution:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        # base case
        if (n == 1):
            return 1
        elif (n == 0):
            return 1
    
        # recursive case
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        