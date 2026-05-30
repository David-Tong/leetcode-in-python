class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        # process
        ans = list()
        ans.append(first)

        for ecd in encoded:
            ans.append(ans[-1] ^ ecd)
        return ans


encoded = [1,2,3]
first = 1

encoded = [6,2,7,3]
first = 4

encoded = [3]
first = 11

solution = Solution()
print(solution.decode(encoded, first))