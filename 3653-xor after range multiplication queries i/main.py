class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        MODULO = 10 ** 9 + 7

        # helper function
        # update
        def update(query):
            l, r, k, v = query
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MODULO
                idx += k

        # process
        for query in queries:
            update(query)

        ans = nums[0]
        for x in range(1, L):
           ans ^= nums[x]
        return ans


nums = [1,1,1]
queries = [[0,2,1,4]]

nums = [2,3,1,5,4]
queries = [[1,4,2,3],[0,2,1,2]]

solution = Solution()
print(solution.xorAfterQueries(nums, queries))
