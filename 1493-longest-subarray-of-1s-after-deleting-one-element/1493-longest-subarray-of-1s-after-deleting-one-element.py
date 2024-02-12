class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        end = 0
        zero_count = 1 if nums[end] == 0 else 0
        
        while end < len(nums) - 1:
            end += 1
            
            if end < len(nums) and nums[end] == 0:
                zero_count += 1
                
            if zero_count > 1:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
                            
        print(start, end, zero_count)
        return end - start
        # return (end - start) if (start != 0 or zero_count != 0) else (end - start - 1)