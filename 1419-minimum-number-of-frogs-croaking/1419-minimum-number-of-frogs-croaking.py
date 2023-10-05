class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croaks = [0,0,0,0,0]
        for c in croakOfFrogs:
            if c == 'c':
                if (croaks[4] > 0):
                    croaks[4] -= 1
                croaks[0] += 1
            elif (c == 'r' and croaks[0] > 0):
                croaks[0] -= 1
                croaks[1] += 1
            elif (c == 'o' and croaks[1] > 0):
                croaks[1] -= 1
                croaks[2] += 1
            elif (c == 'a' and croaks[2] > 0):
                croaks[2] -= 1
                croaks[3] += 1
            elif (c == 'k' and croaks[3] > 0):
                croaks[3] -= 1
                croaks[4] += 1
            else:
                return -1
        for i in range(0,4):
            if croaks[i] != 0:
                return -1
        return croaks[4]