class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_0 = 0
        start = 0
        end = 0
        queue = deque()
        # find initial end with k flips
        while (end < len(nums) and count_0 <= k):
            if (nums[end] == 0):
                count_0 += 1
                queue.append(end)
            end += 1
        end -= 1
        max_len = end - start
        if (count_0 <= k):
            return max_len + 1
        
        # sliding window 
        while (len(queue) > 0 and end < len(nums)):
            start = queue.popleft() + 1
            # print(f"1. start: {start} end: {end}")
            # find next place
            end += 1
            while (end < len(nums)):
                if (nums[end] == 0):
                    queue.append(end)
                    break
                end += 1
            # print(f"2. start: {start} end: {end}")
            if (end - start > max_len):
                max_len = end - start
        
#         if (len(nums) - start > max_len):
#             max_len = len(nums) - start
        return max_len
            
            
            