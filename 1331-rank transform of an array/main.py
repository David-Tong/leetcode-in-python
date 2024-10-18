class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # pre-process
        nums = set()
        for num in arr:
            nums.add(num)
        nums = sorted(nums)

        from collections import defaultdict
        dicts = defaultdict(int)
        for idx, num in enumerate(nums):
            dicts[num] = idx + 1

        # process
        ans = list()
        for num in arr:
            ans.append(dicts[num])
        return ans


arr = [40,10,20,30,10,20]

solution = Solution()
print(solution.arrayRankTransform(arr))
