class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringnum = ''.join([str(d) for d in digits])
        num = int(stringnum) + 1
        stringnum = str(num)
        digits = [*stringnum]
        return [int(d) for d in digits]