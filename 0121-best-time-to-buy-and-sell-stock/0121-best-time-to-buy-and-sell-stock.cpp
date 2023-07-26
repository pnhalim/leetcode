class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        auto buy_it = std::min_element(prices.begin(), prices.end());
        auto sell_it = std::max_element(buy_it, prices.end());
        
        int max_profit = *sell_it - *buy_it;
        
        while (buy_it != prices.begin()) {
            auto old_buy_it = buy_it;
            buy_it = std::min_element(prices.begin(), old_buy_it);
            sell_it = std::max_element(buy_it, old_buy_it);
            
            int profit = *sell_it - *buy_it;
            
            if (profit > max_profit) {
                max_profit = profit;
            }
        }
        
        return max_profit;
    }
};