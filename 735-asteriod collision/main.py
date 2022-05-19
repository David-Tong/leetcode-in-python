class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()

                if stack and stack[-1] > 0 and stack[-1] == abs(asteroid):
                    stack.pop()
                elif stack and stack[-1] > abs(asteroid):
                    pass
                else:
                    stack.append(asteroid)
        return stack


asteroids = [5,10,-5]
asteroids = [8,-8]
asteroids = [10, 2, -5]
asteroids = [5, -5, -5, -10, 5]
#asteroids = [-2,-1,1,2]
#asteroids = [2,1,-2,-1]

solution = Solution()
print(solution.asteroidCollision(asteroids))
