class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # pre-process
        L = len(s)

        # process
        maxi_ones = 0
        maxi_zeros = 0

        pivot = s[0]
        idx_pivot = 0

        idx = 1
        while idx < L:
            if s[idx] != pivot:
                if pivot == '1':
                    maxi_ones = max(maxi_ones, idx - idx_pivot)
                else:
                    maxi_zeros = max(maxi_zeros, idx - idx_pivot)
                pivot = s[idx]
                idx_pivot = idx
            idx += 1
        if pivot == '1':
            maxi_ones = max(maxi_ones, idx - idx_pivot)
        else:
            maxi_zeros = max(maxi_zeros, idx - idx_pivot)

        # post-process
        ans = maxi_ones > maxi_zeros
        return ans


s = "1101"
s = "111000"
s = "110100010"
s = "111"
s = "000"

solution = Solution()
print(solution.checkZeroOnes(s))
