class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        for (int i = 1; i < nums.size(); i++) {
            nums[i] = std::max(nums[i-1] + nums[i], nums[i]);
        }
        
        return *std::max_element(nums.begin(), nums.end());
    }
};
