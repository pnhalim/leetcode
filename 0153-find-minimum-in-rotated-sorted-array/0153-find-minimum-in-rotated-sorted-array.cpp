class Solution {
public:
    int findMin(vector<int>& nums) {
        int i = nums.size() / 2;
        int prev_i = nums.size() - 1;
        while (i > 0) {
            if (nums[i-1] > nums[i]) {
                return nums[i];
            }
            
            if (nums[prev_i] < nums[i]) {
                // somewhere in between
                i = (prev_i + i + 1) / 2;
            }
            else {
                prev_i = i;
                i /= 2;
            }
        }
        return nums[i];
    }
};
