class Solution(object):
    def minMoves(self, balance):
        """
        :type balance: List[int]
        :rtype: int
        """
        # short-cut
        if sum(balance) < 0:
            return -1

        # pre-process
        L = len(balance)
        for x in range(L):
            if balance[x] < 0:
                break
        target = x
        owe = balance[target]

        # process
        idx = L - 1
        step = 1
        ans = 0
        while owe < 0:
            if idx == 1:
                increase = balance[(target + step) % L]
                if owe + increase > 0:
                    ans -= owe * step
                else:
                    ans += increase * step
            else:
                increase = balance[(target + step) % L] + balance[(target - step + L) % L]
                if owe + increase > 0:
                    ans -= owe * step
                else:
                    ans += increase * step
            step += 1
            owe = min(0, owe + increase)
            idx -= 2
        return ans


balance = [5,1,-4]
balance = [1,2,-5,2]
balance = [-3,2]

from random import randint
balance = [randint(0, 10 ** 5) for _ in range(10 ** 4)]
idx = randint(0, 10 ** 4)
balance[idx] *= -1
print(balance)

solution = Solution()
print(solution.minMoves(balance))
