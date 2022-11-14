class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def doReplace(k, grammar):
            if k % 2 == 0:
                if grammar == 0:
                    return 1
                else:
                    return 0
            else:
                if grammar == 0:
                    return 0
                else:
                    return 1

        def doGramar(n, k):
            if n == 1:
                return 0
            else:
                if k % 2 == 1:
                    grammar = doGramar(n - 1, k / 2 + 1)
                else:
                    grammar = doGramar(n - 1, k / 2)
                return doReplace(k, grammar)

        return doGramar(n, k)


n = 1
k = 1

n = 2
k = 1

n = 2
k = 2

n = 30
k = 100000

solution = Solution()
print(solution.kthGrammar(n, k))
