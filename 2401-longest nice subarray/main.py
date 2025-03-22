class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        M = len(bin(10 ** 9)) - 2
        from collections import defaultdict
        dicts = defaultdict(str)

        # process
        # helper
        def getBinary(num):
            binary = bin(num)[2:]
            binary = '0' * (M - len(binary)) + binary
            return binary

        def isValid(mask):
            for x in range(M):
                if mask[x] > 1:
                    return False
            return True

        # sliding window
        left, right = 0, 0
        mask = [0] * M
        ans = 0
        while right < L:
            binary = getBinary(nums[right])
            if nums[right] not in dicts:
                dicts[nums[right]] = binary
            for x in range(M):
                if binary[x] == '1':
                    mask[x] += 1

            while left < right and not isValid(mask):
                if nums[left] in dicts:
                    binary = dicts[nums[left]]
                else:
                    binary = getBinary(nums[left])
                del dicts[nums[left]]
                for x in range(M):
                    if binary[x] == '1':
                        mask[x] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1
        return ans


nums = [1,3,8,48,10]
nums = [3,1,5,11,13]
nums = [1]
nums = [2,4,8,16,32,64,128,256,512,1024,2048]

solution = Solution()
print(solution.longestNiceSubarray(nums))
