class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i, elem in enumerate(nums):
            if i > max_index:
                return False
            if elem + i > max_index:
                max_index = elem + i
        return max_index >= len(nums) - 1