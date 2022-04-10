class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def doCombine(nums, index, combs, k):
            if len(combs) == k:
                self.ans.append(combs[:])
                return
            elif len(nums) - index + len(combs) < k:
                return
            else:
                combs.append(nums[index])
                doCombine(nums, index + 1, combs, k)
                combs.pop(-1)
                doCombine(nums, index + 1, combs, k)

        self.ans = []
        nums = [num for num in range(1, n+1)]
        combs = []
        doCombine(nums, 0, combs, k)
        return self.ans


n = 4
k = 2

n = 1
k = 1

n = 20
k = 2

solution = Solution()
print(solution.combine(n, k))
