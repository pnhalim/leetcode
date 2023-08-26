class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        int target_sum = 0;
        for (int i = 0; i <= nums.size(); i++) {
            target_sum += i;
        }
        
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        
        return target_sum - sum;
    }
};