class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, num in enumerate(nums):
            dicts[num].append(idx)

        # process
        ans = 0
        for num in dicts:
            L = len(dicts[num])
            if L > 1:
                for x in range(L):
                    for y in range(x + 1, L):
                        if dicts[num][x] * dicts[num][y] % k == 0:
                            ans += 1
        return ans


nums = [3,1,2,2,2,1,3]
k = 2

nums = [1,2,3,4]
k = 1

solution = Solution()
print(solution.countPairs(nums, k))
