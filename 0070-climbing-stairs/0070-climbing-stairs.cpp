class Solution {
public:
    int recur_climbStairs(int n, vector<int> &memo) {
        if (memo[n] != 0) {
            return memo[n];
        }
        memo[n] = recur_climbStairs(n-1, memo) + recur_climbStairs(n-2, memo);
        return memo[n];
    }
    
    int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        else if (n == 2) {
            return 2;
        }
        vector<int> memo(n+1);
        memo[0] = 1;
        memo[1] = 1;
        memo[2] = 2;
        return recur_climbStairs(n, memo);
    }
};