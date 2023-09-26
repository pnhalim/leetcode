class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        cur_k = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                cur_k += 1
            # slide left 
            if cur_k > k:
                if nums[left] == 0:
                    cur_k -= 1
                left += 1
        return right - left + 1