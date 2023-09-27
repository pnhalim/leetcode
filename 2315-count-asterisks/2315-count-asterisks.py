class Solution:
    def countAsterisks(self, s: str) -> int:
        total = 0
        pipe = False
        for c in s:
            if c == "*":
                if not pipe:
                    total += 1
            elif c == "|":
                pipe = not pipe


        return total