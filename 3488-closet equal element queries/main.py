class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, num in enumerate(nums):
            dicts[num].append(idx)
        # print(dicts)

        # process
        # helper function
        # distance
        def distance(idx, other):
            return min((idx - other + L) % L, (other -idx + L) % L)

        ans = list()
        for query in queries:
            num = nums[query]
            l = len(dicts[num])
            if l > 1:
                from bisect import bisect_left, bisect_right
                left, right = bisect_left(dicts[num], query), bisect_right(dicts[num], query)
                if left == 0:
                    left = l - 1
                else:
                    left -= 1
                if right == l:
                    right = 0
                # print(left, right, dicts[num][left], dicts[num][right])
                if left != right:
                    ans.append(min(distance(query, dicts[num][left]), distance(query, dicts[num][right])))
                else:
                    ans.append(distance(query, dicts[num][left]))
            else:
                ans.append(-1)
        return ans


nums = [1,3,1,4,1,3,2]
queries = [0,3,5,2]

nums = [1, 2, 3, 4]
queries = [0, 1, 2, 3]

solution = Solution()
print(solution.solveQueries(nums, queries))
