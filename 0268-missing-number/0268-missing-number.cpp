class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        int sum = 0;
        for (int i = 0; i <= nums.size(); i++) {
            sum = sum ^ i;
        }
        
        for (int num : nums) {
            sum = sum ^ num;
        }
        
        return sum;
    }
};