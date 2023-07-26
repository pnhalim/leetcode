class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int best_buy_price = prices[0];
        int best_profit = 0;
        
        for (int i = 0; i < prices.size(); i++) {
            if (best_buy_price > prices[i]) {
                best_buy_price = prices[i];
            }
            else {
                int profit = prices[i] - best_buy_price;
                if (profit > best_profit) {
                    best_profit = profit;
                }
            }
        }
        
        return best_profit;
        
    }
};