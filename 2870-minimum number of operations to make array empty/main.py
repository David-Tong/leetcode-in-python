class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        for num in nums:
            dicts[num] += 1

        # process
        ans = 0
        for num in dicts:
            # divide by 3
            target = dicts[num]
            divby3 = target % 3
            if divby3 == 0:
                ans += target // 3
                continue
            elif divby3 == 1 and target > 3:
                ans += target // 3 - 1
                target -= (target // 3 - 1) * 3
            elif divby3 == 2:
                ans += target // 3
                target -= (target // 3) * 3
            # divide by 2
            if target % 2 == 0:
                ans += target // 2
            else:
                return -1
        return ans


nums = [2,3,3,2,2,4,2,3,4]
nums = [2,1,2,2,3,3]
nums = [2,2]
nums = [3,3,3]
nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]

solution = Solution()
print(solution.minOperations(nums))
