class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr1 = 0
        ptr2 = 0
        
        while (ptr1 < len(nums) and ptr2 < len(nums)):
            if (nums[ptr2] != val):
                nums[ptr1] = nums[ptr2]
                ptr1 += 1
            ptr2 += 1
            
        return ptr1