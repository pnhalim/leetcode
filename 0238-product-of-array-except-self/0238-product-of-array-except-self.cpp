class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int num_zero = 0;
        int product = 1;
        for (int n : nums) {
            if (n == 0) {
                num_zero++;
            }
            else {
                product *= n;
            }
        }
        vector<int> ans;
        for (auto it = nums.begin(); it != nums.end(); it++) {
            if (num_zero > 1) {
                ans.push_back(0);           
            }
            else if (num_zero > 0) {
                if (*it != 0) {
                    ans.push_back(0);
                }
                else {
                    ans.push_back(product);
                }     
            }
            else {
                ans.push_back(product / *it);
            }
        }
        return ans;
    }
};