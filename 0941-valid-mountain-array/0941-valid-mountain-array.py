class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        
        peak = 0
        increasing = True
        
        for i in range(0, len(arr) - 1):
            if arr[i] == arr[i + 1]:
                return False
            
            if increasing:
                if arr[i] > arr[i + 1]:
                    peak = i
                    increasing = False
            else:
                if arr[i] < arr[i + 1]:
                    return False
                
        return peak != 0 and peak != len(arr) - 1