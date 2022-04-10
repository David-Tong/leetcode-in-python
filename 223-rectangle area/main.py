class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        x = ((ax1, ax2), (bx1, bx2))
        y = ((ay1, ay2), (by1, by2))
        x = sorted(x)
        y = sorted(y)

        width = 0
        height = 0
        if x[1][0] < x[0][1]:
            if x[1][1] <= x[0][1]:
                width = x[1][1] - x[1][0]
            else:
                width = x[0][1] - x[1][0]
        if y[1][0] < y[0][1]:
            if y[1][1] <= y[0][1]:
                height = y[1][1] - y[1][0]
            else:
                height = y[0][1] - y[1][0]

        area = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        ans = area + area2
        if area != 0 and area2 != 0:
            ans -= width * height
        return ans


ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2

ax1 = -2
ay1 = -2
ax2 = 2
ay2 = 2
bx1 = -2
by1 = -2
bx2 = 2
by2 = 2

ax1 = 0
ay1 = 0
ax2 = 0
ay2 = 0
bx1 = -1
by1 = -1
bx2 = 1
by2 = 1

ax1 = -3
ay1 = 1
ax2 = -1
ay2 = 3
bx1 = 1
by1 = -2
bx2 = 2
by2 = -1

ax1 = -2
ay1 = -2
ax2 = 2
ay2 = 2
bx1 = -1
by1 = -1
bx2 = 1
by2 = 1

ax1 = -2
ay1 = -2
ax2 = 2
ay2 = 2
bx1 = -1
by1 = 1
bx2 = 1
by2 = 3

solution = Solution()
print(solution.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))
