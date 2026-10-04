class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # pre-process
        L = len(stones)

        presums = list()
        presums.append(0)
        for stone in stones:
            presums.append(presums[-1] + stone)
        # print(presums)

        # process
        from collections import defaultdict
        self.cache = defaultdict(int)

        # dfs - idx start from idx-th element in stones
        #     - return the max score for Alice or Bob in every turn
        def dfs(idx):
            key = "{}".format(idx)
            if key in self.cache:
                return self.cache[key]

            if idx == L - 1:
                return 0
            else:
                min_max = float("-inf")
                idx += 1
                while idx < L:
                    score = presums[idx + 1]
                    min_max = max(min_max, score - dfs(idx))
                    idx += 1
                self.cache[key] = min_max
                return min_max

        ans = dfs(0)
        return ans


stones = [-1,2,-3,4,-5]
stones = [7,-6,5,10,5,-2,-6]
stones = [-10,-12]

from random import randint
stones = [randint(-10 ** 4, 10 ** 4) for _ in range(10 ** 5)]
print(stones)

solution = Solution()
print(solution.stoneGameVIII(stones))
