class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        from math import sqrt
        limit = int(sqrt(area)) + 1

        ans = list()
        mini = float("inf")
        for w in range(1, limit):
            if area % w == 0:
                l = area / w
                if w > l:
                    break
                else:
                    gap = l - w
                    if gap == 0:
                        return (l, w)
                    else:
                        if gap < mini:
                            mini = gap
                            ans = [l, w]
        return ans


area = 4
area = 37
area = 122122
area = 10 ** 7

solution = Solution()
print(solution.constructRectangle(area))
