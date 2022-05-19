class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.anses = []

        def doSum(k, n, idx, selected):
            if idx > 10:
                return

            total = sum(selected)
            if len(selected) == k and total == n:
                self.anses.append(selected[:])
                return
            elif len(selected) > k or total > n:
                return

            doSum(k, n, idx + 1, selected + [idx])
            doSum(k, n, idx + 1, selected)

        doSum(k, n, 1, [])
        return self.anses


k = 3
n = 7

k = 3
n = 9

k = 4
n = 1

k = 2
n = 1

k = 9
n = 45

solution = Solution()
print(solution.combinationSum3(k, n))
