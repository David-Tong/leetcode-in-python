class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        # pre-process
        hBars, vBars = sorted(hBars), sorted(vBars)

        # help function
        def getMax(arr):
            idx = 0
            res = 1
            con = 1
            # print(arr)
            while idx < len(arr) - 1:
                if arr[idx] + 1 == arr[idx + 1]:
                    con += 1
                else:
                    res = max(res, con)
                    con = 1
                idx += 1
            res = max(res, con)
            # print(res)
            return res

        # process
        ans = (min(getMax(hBars), getMax(vBars)) + 1) ** 2
        return ans


"""
n = 2
m = 1
hBars = [2,3]
vBars = [2]
"""

"""
n = 1
m = 1
hBars = [2]
vBars = [2]
"""

n = 2
m = 3
hBars = [2,3]
vBars = [2,4]

from random import randint
n = randint(1, 10 ** 8)
m = randint(1, 10 ** 8)
hBars = list(set(randint(2, n + 1) for _ in range(100)))
vBars = list(set(randint(2, m + 1) for _ in range(100)))
print(n)
print(m)
print(hBars)
print(vBars)

solution = Solution()
print(solution.maximizeSquareHoleArea(n, m, hBars, vBars))
