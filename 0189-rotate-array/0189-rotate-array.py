class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Solution 1 - Temp Array
        # O(n) time, O(k) space
        k = k % len(nums)
        arr = nums[len(nums)-k:len(nums)]
        for i in range(len(nums)-1,k-1,-1):
            nums[i] = nums[i-k]
        for i in range(k):
            nums[i] = arr[i]
        
#         # Solution 2 - Bubble k Times
#         # O(nk) time, O(1) space
#         def swap(i,j):
#             temp = nums[i]
#             nums[i] = nums[j]
#             nums[j] = temp
#         for _ in range(k):
#             for i in range(len(nums)-1,0,-1):
#                 swap(i, i-1)        
    
#         # Solution 3 - Reverse
#         # O(n) time, O(1) space
#         def reverse(start, end):
#             end -= 1
#             while (start < end):
#                 temp = nums[start]
#                 nums[start] = nums[end]
#                 nums[end] = temp
#                 start += 1
#                 end -= 1
#         k = k % len(nums)
#         reverse(0, len(nums))
#         reverse(0, k)
#         reverse(k, len(nums))

        