class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            while len(stack) > 0 and asteroids[i] < 0 and stack[-1] >= 0:
                if -asteroids[i] > stack[-1]:
                    stack.pop()
                else:
                    break
            else:
                if len(stack) == 0 or -asteroids[i] > stack[-1]:
                    stack.append(asteroids[i])
                elif -asteroids[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(asteroids[i])

        return stack
    
    def asteroidCollision2(self, asteroids):
        stack = []
        for new in asteroids:
            while stack and new < 0 < stack[-1]:
                if stack[-1] < -new:
                    stack.pop()
                    continue
                elif stack[-1] == -new:
                    stack.pop()
                break
            else:
                stack.append(new)
        return stack
    




asteroids = [1,-2,-2,-2]
print(Solution().asteroidCollision2(asteroids))