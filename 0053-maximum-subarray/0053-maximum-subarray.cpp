class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max = nums[0];
        int currSum = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            currSum = std::max(currSum + nums[i], nums[i]);
            if (currSum > max) {
                max = currSum;
            }
        }
        
        return max;
    }
};
