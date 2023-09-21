class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
        unordered_set<int> prev;
        prev.insert(amount);
        
        int count = 0;
        unordered_set<int> next;
        
        while (!prev.empty() && prev.find(0) == prev.end()) {
            for (int v : prev) {
                for (int c : coins) {
                    if (v-c >= 0 && prev.find(v-c) == prev.end()) {
                        next.insert(v-c);
                    }
                }
            }
            prev = next;
            next.clear();
            count++;
        }
        
        if (prev.empty()) {
            return -1;
        }
        
        return count;
        
    }
};