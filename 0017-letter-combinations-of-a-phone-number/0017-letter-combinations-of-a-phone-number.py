class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if len(digits) == 0:
            return ans
        
        def getLetters(digit: str):
            if digit == '2':
                return ('a', 'b', 'c')
            elif digit == '3':
                return ('d', 'e', 'f')
            elif digit == '4':
                return ('g', 'h', 'i')
            elif digit == '5':
                return ('j', 'k', 'l')
            elif digit == '6':
                return ('m', 'n', 'o')
            elif digit == '7':
                return ('p', 'q', 'r', 's')
            elif digit == '8':
                return ('t', 'u', 'v')
            else:
                return ('w', 'x', 'y', 'z')
        
        # initial fill with first letter
        for letter in getLetters(digits[0]):
            ans.append(letter)
            
        # bfs for all remaining letters
        for digit in digits[1:]:
            bfs = ans
            ans = []
            while len(bfs) > 0:
                pre = bfs.pop()
                new = getLetters(digit)
                for letter in new:
                    ans.append(pre + letter)
        
        return ans