class Solution(object):
    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        L = 100

        from collections import defaultdict
        presums = defaultdict(list)
        for x in range(1, L + 1):
            presums[x].append(0)
        for num in nums:
            for x in range(1, L + 1):
                if x == num:
                    presums[x].append(presums[x][-1] + 1)
                else:
                    presums[x].append(presums[x][-1])

        def hasValue(num, query):
            return presums[num][query[1] + 1] - presums[num][query[0]] > 0

        # process
        ans = list()
        for query in queries:
            prev = -1
            curr = 1
            mini = L
            while curr <= L:
                if hasValue(curr, query):
                    if prev != -1:
                        mini = min(mini, curr - prev)
                    prev = curr
                curr += 1
            if mini == L:
                ans.append(-1)
            else:
                ans.append(mini)
        return ans


nums = [1,3,4,8]
queries = [[0,1],[1,2],[2,3],[0,3]]

nums = [4,5,2,2,7,10]
queries = [[2,3],[0,2],[0,5],[3,5]]

solution = Solution()
print(solution.minDifference(nums, queries))
