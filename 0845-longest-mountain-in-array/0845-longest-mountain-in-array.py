class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        longest = 0
        start = peak = end = 0

        while start < len(arr) - 1:
            
            # find start
            if arr[start] < arr[start + 1]:
                # find peak
                peak = start
                while peak < len(arr) - 1 and arr[peak] < arr[peak + 1]:
                    peak += 1
                # not a valid tree
                if peak == start:
                    start = max(start + 1, peak)
                    continue

                # find end 
                end = peak
                while end < len(arr) - 1 and arr[end] > arr[end + 1]:
                    end += 1
                if peak == end:
                    start = max(start + 1, end)
                    continue

                # record the length
                longest = max(longest, end - start + 1)
            
            start = max(start + 1, end)

        return longest