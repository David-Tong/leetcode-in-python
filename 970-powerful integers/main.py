class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        # conner case
        if bound == 0:
            return list()

        # pre-process
        from math import log
        M = 1 if x == 1 else int(log(bound, x)) + 1
        N = 1 if y == 1 else int(log(bound, y)) + 1

        # process
        ans = set()
        for m in range(M):
            for n in range(N):
                powerful = x ** m + y ** n
                if powerful <= bound:
                    ans.add(powerful)
        return list(ans)


x = 2
y = 3
bound = 10

x = 3
y = 5
bound = 15

x = 2
y = 1
bound = 10

x = 2
y = 3
bound = 0

solution = Solution()
print(solution.powerfulIntegers(x, y, bound))
