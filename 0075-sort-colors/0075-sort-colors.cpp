class Solution {
public:
    void sortColors(vector<int>& nums) {
        int left = 0;                   // stores first nonzero
        int right = nums.size() - 1;    // stores last non-two
        int current = 0;                // current 
        
        while (current <= right) {
            if (nums[current] == 0) {
                swap(nums[left], nums[current]);
                left++;
                current++;
            }
            else if (nums[current] == 2) {
                swap(nums[current], nums[right]);
                right--;
            }
            else {
                current++;
            }
        }
        
    }
};

