class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(encoded)
        xors = 0
        for x in range(L + 1):
            xors ^= x + 1

        others = 0
        for x in range(1, L, 2):
            others ^= encoded[x]

        first = xors ^ others
        # print(first)

        # process
        ans = list()
        ans.append(first)
        for x in range(L):
            ans.append(ans[-1] ^ encoded[x])
        return ans


encoded = [3,1]
encoded = [6,5,4,6]

solution = Solution()
print(solution.decode(encoded))