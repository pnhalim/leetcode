class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tail = 0
        count = 1
        for i in range(1, len(nums)):
            if (nums[i] == nums[i-1]):
                if (count < 2):
                    tail += 1
                    count += 1
            else:
                count = 1
                tail += 1
                
            nums[tail] = nums[i]
            
        return tail + 1
        
