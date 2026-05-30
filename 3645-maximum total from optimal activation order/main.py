class Solution(object):
    def maxTotal(self, value, limit):
        """
        :type value: List[int]
        :type limit: List[int]
        :rtype: int
        """
        # pre-process
        L = len(limit)
        taken = [False] * L
        pairs = zip(limit, value)
        pairs = sorted(pairs, key=lambda x: (x[0], -x[1]))
        # print(pairs)

        # process
        idx = 0
        idx2 = 0
        active = 0
        ans = 0
        while idx < L:
            if active < pairs[idx][0]:
                ans += pairs[idx][1]
                taken[idx] = True
                active += 1
            sub = 0
            while idx2 < L and pairs[idx2][0] <= active:
                if taken[idx2]:
                    sub += 1
                idx2 += 1
            active -= sub
            idx = max(idx + 1, idx2)
        return ans


value = [3,5,8]
limit = [2,1,3]

value = [4,2,6]
limit = [1,1,1]

value = [4,1,5,2]
limit = [3,3,2,3]

from random import randint
value = [randint(1, 10 ** 3) for _ in range(10 ** 3)]
limit = [randint(1, 10 ** 2) for _ in range(10 ** 3)]
print(value)
print(limit)

solution = Solution()
print(solution.maxTotal(value, limit))
