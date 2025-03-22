class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # helper
        def binarize(num):
            binary = [0] * L
            idx = 0
            while num:
                binary[idx] = num & 1
                num >>= 1
                idx += 1
            return binary

        # pre-process
        L = 30
        M = len(nums1)
        N = len(nums2)
        binary1 = [0] * L
        for num1 in nums1:
            binary = binarize(num1)
            for x in range(L):
                binary1[x] += binary[x]

        binary2 = [0] * L
        for num2 in nums2:
            binary = binarize(num2)
            for x in range(L):
                binary2[x] += binary[x]

        # process
        binary = [0] * L
        for x in range(L):
            binary[x] = (binary1[x] * N + binary2[x] * M) % 2

        # post-process
        idx = 0
        ans = 0
        while idx < L:
            ans += binary[idx] * (2 ** idx)
            idx += 1
        return ans


nums1 = [2,1,3]
nums2 = [10,2,5,0]

nums1 = [1,2]
nums2 = [3,4]

nums1 = [1]
nums2 = [999]

solution = Solution()
print(solution.xorAllNums(nums1, nums2))
