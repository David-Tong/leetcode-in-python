class Solution(object):
    def minOperations(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: int
        """
        # pre-process
        fours = list()
        fours.append(0)
        k = 0
        four = 4 ** k * 3
        while four <= 10 ** 9:
            fours.append(four)
            k += 1
            four = 4 ** k * 3
        # print(fours)

        groups = list()
        presums = list()
        for idx, four in enumerate(fours):
            if idx == 0:
                presums.append(idx * fours[idx])
                groups.append(0)
            else:
                presums.append(presums[-1] + idx * fours[idx])
                groups.append(groups[-1] + fours[idx])
        # print(presums)
        # print(groups)

        # helper function
        # count
        from collections import defaultdict
        self.cache = defaultdict(int)
        self.cache[0] = 0

        def count(n):
            if n in self.cache:
                return self.cache[n]
            from bisect import bisect_left
            idx = bisect_left(groups, n)
            res = presums[idx - 1] + (n - groups[idx - 1]) * idx
            self.cache[n] = res
            return res

        # process
        ans = 0
        for query in queries:
            ans += (count(query[1]) - count(query[0] - 1) + 1) // 2
        return ans


queries = [[1,2],[2,4]]
queries = [[2, 6]]

from random import randint
def pair():
    a, b = randint(1, 10 ** 9), randint(1, 10 ** 9)
    return [min(a, b), max(a, b)]

queries = [pair() for _ in range(10 ** 5)]
# print(queries)
queries = [[1, 8]]

solution = Solution()
print(solution.minOperations(queries))
