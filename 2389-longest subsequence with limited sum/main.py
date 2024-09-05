class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        N = len(nums)

        nums = sorted(nums)
        sums = [0] * N
        sumi = 0
        for idx, num in enumerate(nums):
            sumi += num
            sums[idx] = sumi

        M = len(queries)
        anses = [0] * M
        from bisect import bisect_right
        for idx, query in enumerate(queries):
            anses[idx] = bisect_right(sums, query)
        return anses


nums = [4,5,2,1]
queries = [3,10,21]

nums = [2,3,4,5]
queries = [1]

solution = Solution()
print(solution.answerQueries(nums, queries))
