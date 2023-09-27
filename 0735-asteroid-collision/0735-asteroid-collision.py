class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            
            # empty -> add
            if (len(stack) == 0):
                stack.append(asteroids[i])
                continue
                
            # asteroid is going same direction -> add 
            if (asteroids[i] * stack[-1] > 0):
                stack.append(asteroids[i])
                continue
            
            if (asteroids[i] > abs(stack[-1])):
                stack.append(asteroids[i])
            else: # (asteroids[i] < 0 and abs(asteroids[i]) >= abs(stack[-1])):
                # asteroid is larger and going left -> go as far left as possible
                while (len(stack) > 0 and stack[-1] > 0 
                      and abs(asteroids[i]) > abs(stack[-1])):
                    stack.pop()
                if (len(stack) > 0 and stack[-1] > 0 
                    and abs(asteroids[i]) == abs(stack[-1])):
                    stack.pop()
                    continue
                if (len(stack) == 0 or stack[-1] < abs(asteroids[i])):
                    stack.append(asteroids[i])
            
            # asteroid is smaller and going left -> do nothing
        return stack