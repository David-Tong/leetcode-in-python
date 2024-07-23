class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        xors = list()
        for num in nums:
            xors.append((num ^ k) - num)
        xors = sorted(xors, reverse=True)
        print(xors)

        # process
        increase = 0
        for x in range(0, L, 2):
            if x + 1 < L and xors[x] + xors[x + 1] > 0:
                increase += xors[x] + xors[x + 1]
            else:
                break
        ans = sum(nums) + increase
        return ans


nums = [1,2,1]
k = 3
edges = [[0,1],[0,2]]

nums = [2,3]
k = 7
edges = [[0,1]]

nums = [7,7,7,7,7,7]
k = 3
edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]

solution = Solution()
print(solution.maximumValueSum(nums, k, edges))
