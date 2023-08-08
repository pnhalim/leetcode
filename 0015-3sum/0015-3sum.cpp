class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        set<vector<int>> ans;
        for (int i = 0; i < nums.size() - 2; i++) {
            int j = i + 1;
            int k = nums.size() - 1;
            
            while (i < j && i < k && j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    ans.insert({nums[i], nums[j], nums[k]});
                    j++;
                    k--;
                    
                    // eliminate duplicates
                    while (0 < j && j < nums.size() && nums[j] == nums[j-1]) { j++; }
                    while (0 < k && k < nums.size() && nums[k] == nums[k+1]) { k--; }
                    // cout << i << j << k << endl;
                }
                else if (sum < 0) {
                    j++;
                }
                else {
                    k--;
                }
            }
        }
        
        return vector<vector<int>>(ans.begin(), ans.end());
    }
};