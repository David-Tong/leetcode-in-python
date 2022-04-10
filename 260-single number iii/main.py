class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 2:
            return nums

        xor = 0
        for num in nums:
            xor ^= num

        # the size will be limited to 3
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            key = num ^ xor
            dicts[key] += 1

        ans = []
        if len(dicts) == 2:
            ans = dicts.key()
        else:
            for key in dicts:
                if dicts[key] == 1:
                    ans.append(key)
        return ans


nums = [1,2,1,3,2,5]
nums = [-1,0]
nums = [0,1]
nums = [5,7,8,9,11,11,7,6,5,8]

solution = Solution()
print(solution.singleNumber(nums))
