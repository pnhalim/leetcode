class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        peak = 0
        increasing = True
        for i in range(0, len(arr) - 1):
            if increasing:
                if arr[i] > arr[i+1]:
                    increasing = False
                    peak = i
                elif arr[i] == arr[i+1]:
                    return False
            elif not increasing:
                if arr[i] < arr[i+1] or arr[i] == arr[i+1]:
                    return False
                
        return peak != 0