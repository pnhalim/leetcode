class Solution:
    def jump(self, nums: List[int]) -> int:
        # preprocess array, each elem stores the max index that it can go or anything before it can go
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1], i+nums[i])
        
        # iterate through array, go highest each time and inc count because highest jump is stored
        count = 0
        i = 0
        while (i < len(nums) - 1):
            i = nums[i]
            count += 1
        
        return count
        
# [2,3,1,1,4]

# [2,4,4,4,8]

# [2,4]