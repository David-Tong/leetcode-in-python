class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        # process
        if abs(x - z) < abs(y - z):
            return 1
        elif abs(x - z) == abs(y - z):
            return 0
        else:
            return 2


x = 2
y = 7
z = 4

x = 2
y = 5
z = 6

x = 1
y = 5
z = 3

solution = Solution()
print(solution.findClosest(x, y, z))
