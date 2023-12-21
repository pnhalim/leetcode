class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        longest = 0
        
        start = 0
        peak = 0
        end = 0
        
        # find mountains
        while end < len(arr) - 1:
            
            # find start
            while start < len(arr) - 1:
                if arr[start] < arr[start + 1]:
                    break
                start += 1
            peak = start
            end = start

            # find peak
            while peak < len(arr) - 1:
                if arr[peak] > arr[peak + 1]:
                    break
                elif arr[peak] == arr[peak + 1]:
                    start = peak
                    end = peak
                    break
                peak += 1
            if start == peak:
                continue
            end = peak
            
            # find end
            while end < len(arr) - 1:
                print(start, peak, end)
                if (arr[end] < arr[end + 1] 
                    or arr[end] == arr[end + 1]):
                    break
                end += 1
            
            if start != peak and peak != end:
                longest = max(longest, end - start + 1)
            start = end

        return longest