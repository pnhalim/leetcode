class Solution {
public:
    int search(vector<int>& nums, int target) {
        // find pivot (min index)
        int left = 0;
        int right = nums.size() - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            }
            else {
                right = mid;
            }
        }
        if (nums[(left - 1) % nums.size()] < nums[left]) {
            left = (left + 1) % nums.size();
        }
        cout << left;
        
        // binary search
        int offset = left;
        left = offset;
        right = nums.size() - 1 + offset;
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid % nums.size()] < target) {
                left = mid + 1;
            }
            else {
                right = mid;
            }
        }
        
        if (nums[left % nums.size()] == target) {
            return left % nums.size();
        }       
        return -1;
    }
};
