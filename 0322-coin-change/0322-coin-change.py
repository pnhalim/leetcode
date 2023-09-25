class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def recurse(m) -> int:
            # dp
            if m in memo.keys():
                return memo[m]
            
            # base case
            if m == 0:
                return 0
            elif m in coins:
                return 1
            elif m < 0:
                return float('inf')
            
            # try each coin
            min_count = float('inf')
            for c in coins:
                if m-c > 0:
                    memo[m-c] = recurse(m-c)
                    if memo[m-c] < min_count:
                        min_count = memo[m-c]
            if min_count == float('inf'):
                return float('inf')
            return min_count + 1
        
        ans = recurse(amount)
        return ans if ans != float('inf') else -1