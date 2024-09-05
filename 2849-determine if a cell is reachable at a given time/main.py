class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        if sx == fx and sy == fy and t == 1:
            return False

        steps = max(abs(sx - fx), abs(sy - fy))
        return True if steps <= t else False


sx = 2
sy = 4
fx = 7
fy = 7
t = 6

sx = 1
sy = 2
fx = 1
fy = 2
t = 1

solution = Solution()
print(solution.isReachableAtTime(sx, sy, fx, fy, t))
