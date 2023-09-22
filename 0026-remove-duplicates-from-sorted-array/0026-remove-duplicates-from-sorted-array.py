class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        currptr = 0
        sortptr = 1
        prev = nums[currptr]
        num = 1
        
        while (currptr < len(nums) and sortptr < len(nums)):
            if (prev != nums[sortptr]):
                currptr += 1
                nums[currptr] = nums[sortptr]
                prev = nums[sortptr]
                num += 1
            sortptr += 1
            
        return num