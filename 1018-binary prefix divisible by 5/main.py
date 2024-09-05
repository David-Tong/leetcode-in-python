class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        L = len(nums)
        nums = [str(_) for _ in nums]

        ans = list()
        for x in range(L):
            number = int("".join(nums[:x + 1]), base=2)
            # print("number - {}".format(number))
            if number % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans


nums = [1,0,1]
nums = [0,1,1]
nums = [1,1,1]

solution = Solution()
print(solution.prefixesDivBy5(nums))
