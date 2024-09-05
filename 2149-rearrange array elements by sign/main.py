class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positives = list()
        negatives = list()

        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)

        L = len(positives)
        ans = list()
        for x in range(L):
            ans.append(positives[x])
            ans.append(negatives[x])
        return ans


nums = [3,1,-2,-5,2,-4]
nums = [-1,1]

solution = Solution()
print(solution.rearrangeArray(nums))
