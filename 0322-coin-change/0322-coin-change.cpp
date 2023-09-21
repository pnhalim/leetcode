class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
        vector<int> dp(amount+1, INT_MAX);
        dp[0] = 0;
        
        for (int i = 0; i <= amount; i++) {
            // fill dp with amounts st dp[amount] = min num coins
            if (dp[i] != INT_MAX) {
                for (int c : coins) {
                    if (c <= amount && i+c <= amount) {
                        dp[i+c] = min(dp[i+c], dp[i] + 1);
                    }
                }
            }
        }
        
        if (dp[amount] != INT_MAX) {
                return dp[amount];
            }
        return -1;
    }
};