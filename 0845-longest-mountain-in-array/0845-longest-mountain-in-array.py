class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        longest = 0
        start = peak = end = 0
        
        [1,2,3,4,5,5,6,7,6,5,4,3]
        
        # find the correct start and ++ (must be decreasing)
        while start < len(arr) - 1:
            
            if arr[start] < arr[start + 1]:
                # find the peak 
                peak = start
                while peak < len(arr) - 1:
                    if arr[peak] > arr[peak + 1]:
                        break
                    elif arr[peak] == arr[peak + 1]:
                        start = peak
                        break
                    peak += 1
                # check if peak is valid
                if start == peak:
                    start += 1
                    continue

                # find the end
                end = peak
                while end < len(arr) - 1:
                    if (arr[end] < arr[end + 1] 
                        or arr[end] == arr[end + 1]):
                        break
                    end += 1

                # record longest and start = end
                if start != peak and peak != end:
                    # valid mountain
                    longest = max(longest, end - start + 1)
                start = end
                
            else:
                start += 1
            
        return longest
        
        