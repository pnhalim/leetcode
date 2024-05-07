class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # def swap(j, k):
        #     temp = nums[j]
        #     nums[j] = nums[k]
        #     nums[k] = temp
        
        k = k % len(nums)
        arr = nums[len(nums)-k:len(nums)]
        for i in range(len(nums)-1,k-1,-1):
            nums[i] = nums[i-k]
        for i in range(k):
            nums[i] = arr[i]
        
        
# [1,2,3,4,5,6,7]
# [5,6,7,1,2,3,4]
