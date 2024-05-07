class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tail = 0
        has_two = False
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if has_two == False:
                    tail += 1
                    has_two = True
            else:
                has_two = False
                tail += 1
                
            nums[tail] = nums[i]
            
        return tail + 1
        
