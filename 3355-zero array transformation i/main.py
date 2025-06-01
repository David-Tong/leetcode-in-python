class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        # pre-process
        L = len(nums)
        subs, adds = list(), list()
        for query in queries:
            subs.append(query[0])
            if query[1] < L - 1:
                adds.append(query[1] + 1)
        subs, adds = sorted(subs), sorted(adds)

        differences = [0] * L
        for sub in subs:
            differences[sub] -= 1
        for add in adds:
            differences[add] += 1
        # print(differences)

        # process
        difference = 0
        for x in range(L):
            difference += differences[x]
            if nums[x] + difference > 0:
                return False
        return True


nums = [1,0,1]
queries = [[0,2]]

nums = [4,3,2,1]
queries = [[1,3],[0,2]]

solution = Solution()
print(solution.isZeroArray(nums, queries))
