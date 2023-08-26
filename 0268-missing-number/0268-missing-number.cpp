class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // O(n) space O(n) runtime
        unordered_set<int> nums_set(nums.begin(), nums.end());
        for (int i = 0; i <= nums.size(); i++) {
            if (nums_set.find(i) == nums_set.end()) {
                return i;
            }
        }
        // error
        return -1;
    }
};