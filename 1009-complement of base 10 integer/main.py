class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # process
        binary = bin(n)[2:]
        complement = ""
        for b in binary:
            if b == "1":
                complement += "0"
            else:
                complement += "1"
        ans = int(complement, 2)
        return ans


n = 5
n = 7
n = 10

solution = Solution()
print(solution.bitwiseComplement(n))