class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        if L == 1:
            return nums
        combined = zip(nums, [_ for _ in range(L)])
        combined = sorted(combined)

        groups = list()
        group = list()
        for x in range(1, L):
            group.append(combined[x - 1])
            if combined[x][0] - combined[x - 1][0] > limit:
                groups.append(group)
                group = list()
        group.append(combined[x])
        groups.append(group)

        # process
        ans = [0] * L
        for group in groups:
            idxes = sorted([_[1] for _ in group])
            for x in range(len(group)):
                ans[idxes[x]] = group[x][0]
        return ans


nums = [1,5,3,9,8]
limit = 2

nums = [1,7,6,18,2,1]
limit = 3

nums = [1,7,28,19,10]
limit = 3

nums = [1]
limit = 3

nums = [10, 100, 500, 700, 1000]
limit = 1

solution = Solution()
print(solution.lexicographicallySmallestArray(nums, limit))
