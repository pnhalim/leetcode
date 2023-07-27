class Solution {
public:
    int maxProduct(vector<int>& nums) {        
        int currPos = 0;
        int currNeg = 0;
        
        for (int i = 0; i < nums.size(); i++) {
                        
            if (nums[i] >= 0) {
                currPos = max(currPos * nums[i], nums[i]);
                currNeg = currNeg * nums[i];
            }
            else {
                int tempPos = currNeg * nums[i];
                currNeg = min(currPos * nums[i], nums[i]);
                currPos = tempPos;
            }
            
            nums[i] = (currPos > 0) ? currPos : currNeg; 
        }
        
        return *max_element(nums.begin(), nums.end());
    }
};


