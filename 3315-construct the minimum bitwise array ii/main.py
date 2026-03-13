class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        # helper function
        def find(target):
            binary = bin(target)[2:]
            idx = len(binary) - 1
            while idx >= 0:
                if binary[idx] == '0':
                    break
                idx -= 1
            if idx == 0:
                binary = binary[1:]
            else:
                binary = binary[:idx + 1] + '0' + binary[idx + 2:]
            res = int(binary, 2)
            return res

        # process
        ans = list()
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
            else:
                ans.append(find(num))
        return ans


nums = [2,3,5,7]
nums = [11,13,31]
nums = [491, 827, 991]
nums = [1275823, 1299359, 1299827]

solution = Solution()
print(solution.minBitwiseArray(nums))