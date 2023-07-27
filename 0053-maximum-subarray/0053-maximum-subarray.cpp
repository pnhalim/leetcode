class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            nums[i] = std::max(nums[i-1] + nums[i], nums[i]);
            if (nums[i] > max) {
                max = nums[i];
            }
        }
        
        return max;
    }
};
