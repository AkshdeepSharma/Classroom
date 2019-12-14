class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            if asteroid > 0 or not stack:
                stack.append(asteroid)
            elif asteroid < 0:
                while stack and stack[-1] > 0:
                    if stack[-1] == asteroid * -1:
                        stack.pop()
                        break
                    elif stack[-1] > asteroid * -1:
                        break
                    else:
                        stack.pop()
                        continue
                else:
                    stack.append(asteroid)
        return stack
