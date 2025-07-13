class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        idxes = list()
        for x in range(L):
            if nums[x] == key:
                idxes.append(x)

        # process
        ans = set()
        for idx in idxes:
            for x in range(max(0, idx - k), min(L, idx + k + 1)):
                ans.add(x)
        ans = sorted(list(ans))
        return ans


nums = [3,4,9,1,3,9,5]
key = 9
k = 1

nums = [2,2,2,2,2]
key = 2
k = 2

solution = Solution()
print(solution.findKDistantIndices(nums, key, k))
