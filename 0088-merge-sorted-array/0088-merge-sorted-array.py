class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        other_nums1 = nums1[:m]
        left = 0
        right = 0
        while (left < m  and right < n):
            if other_nums1[left] < nums2[right]:
                nums1[left + right] = other_nums1[left]
                left += 1
            else:
                nums1[left + right] = nums2[right]
                right += 1
        while (left < m):
            nums1[left + right] = other_nums1[left]
            left += 1
        while (right < n):
            nums1[left + right] = nums2[right]
            right += 1
            
            
        
        