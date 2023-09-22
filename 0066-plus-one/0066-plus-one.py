class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = (digits[-1] + 1) // 10
        digits[-1] = (digits[-1] + 1) % 10
        
        i = len(digits) - 1
        
        if (carry and i == 0):
            digits.insert(0, 1)
            return digits
        
        while (carry):
            if (i == 0):
                digits.insert(0, 1)
                return digits
            print(digits[i])
            carry = (digits[i-1] + 1) // 10
            digits[i-1] = (digits[i-1] + 1) % 10
            i = i-1
            
        return digits
            