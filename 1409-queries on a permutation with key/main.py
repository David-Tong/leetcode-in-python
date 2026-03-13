class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        # pre-process
        nums = [x + 1 for x in range(m)]
        def move(target):
            idx = 0
            while idx < m:
                if target == nums[idx]:
                    nums.pop(idx)
                    nums.insert(0, target)
                    return idx
                idx += 1

        # process
        ans = list()
        for query in queries:
            ans.append(move(query))
        return ans


queries = [3,1,2,1]
m = 5

queries = [4,1,2,2]
m = 4

queries = [7,5,5,8,3]
m = 8

from random import randint
m = 10 ** 3
queries = [randint(1, m) for _ in range(m)]
print(queries)

solution = Solution()
print(solution.processQueries(queries, m))
