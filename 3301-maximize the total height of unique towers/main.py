class Solution(object):
    def maximumTotalSum(self, maximumHeight):
        """
        :type maximumHeight: List[int]
        :rtype: int
        """
        # pre-process
        L = len(maximumHeight)
        maximumHeight = sorted(maximumHeight, reverse = True)

        # process
        height = maximumHeight[0]
        cap = height - 1
        ans = height
        idx = 1
        while idx < L:
            height = min(cap, maximumHeight[idx])
            ans += height
            if cap == 0:
                return -1
            cap = height - 1
            idx += 1
        return ans


maximumHeight = [2,3,4,3]
maximumHeight = [15,10]
maximumHeight = [2,2,1]

from random import randint
maximumHeight = [randint(1, 10 ** 6) for _ in range(10 ** 5)]
print(maximumHeight)

solution = Solution()
print(solution.maximumTotalSum(maximumHeight))
