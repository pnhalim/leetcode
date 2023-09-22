class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aptr = len(a)-1
        bptr = len(b)-1
        
        ans = []
        carry = 0
        while (aptr >= 0 and bptr >= 0):
            val = carry + int(a[aptr]) + int(b[bptr])
            carry = val // 2
            ans.append(str(val % 2))
            aptr -= 1
            bptr -= 1
        while (aptr >= 0):
            val = carry + int(a[aptr])
            carry =  val // 2
            ans.append(str(val % 2))
            aptr -= 1
        while (bptr >= 0):
            val = carry + int(b[bptr])
            carry = val // 2
            ans.append(str(val % 2))
            bptr -= 1
        if (carry):
            ans.append(str(carry))
        return ''.join(ans)[::-1]