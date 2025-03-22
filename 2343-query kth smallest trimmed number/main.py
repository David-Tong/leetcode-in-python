class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums[0])
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, num in enumerate(nums):
            for x in range(1, L + 1):
                dicts[x].append((int(num[-x:]), idx))

        for key in dicts:
            dicts[key] = sorted(dicts[key])

        # process
        ans = list()
        for query in queries:
            ans.append(dicts[query[1]][query[0] - 1][1])
        return ans


nums = ["102","473","251","814"]
queries = [[1,1],[2,3],[4,2],[1,2]]

nums = ["24","37","96","04"]
queries = [[2,1],[2,2]]

solution = Solution()
print(solution.smallestTrimmedNumbers(nums, queries))
