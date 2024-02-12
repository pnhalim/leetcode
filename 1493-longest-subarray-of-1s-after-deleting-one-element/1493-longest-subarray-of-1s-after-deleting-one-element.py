class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        mid = 0
        end = 0
        max_len = 0
        
        while end < len(nums):
            if nums[start] == 0:
                start += 1
                mid = start
                end = start
            elif nums[mid] == 1:
                mid += 1
                end = mid + 1
            elif nums[end] == 0:
                max_len = max(max_len, end - 1 - start)
                start = mid + 1
                mid = mid + 1
                end = mid + 1
            elif nums[end] == 1:
                end += 1

        max_len = max(max_len, end - 1 - start)
        while mid < len(nums) and nums[mid] == 1:
            mid += 1
        max_len = max(max_len, mid - start)
        
        
        return max_len - 1 if (start == 0 and max_len == mid - start) else max_len