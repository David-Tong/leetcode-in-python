class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        self.anses = set()

        def doConsec(seq, n, k):
            if n == 0:
                self.anses.add(seq)
            else:
                # add k
                result = int(seq[-1]) + k
                if 0 <= result <= 9:
                    doConsec(seq + str(result), n - 1, k)

                # minus k
                result = int(seq[-1]) - k
                if 0 <= result <= 9:
                    doConsec(seq + str(result), n - 1, k)

        for x in range(1, 10):
            doConsec(str(x), n - 1, k)

        return sorted(self.anses)


n = 3
k = 7

n = 2
k = 1

n = 9
k = 3

solution = Solution()
print(solution.numsSameConsecDiff(n, k))
