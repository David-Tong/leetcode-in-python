class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)

        target = (alice_sum + bob_sum) / 2

        alice_diff = alice_sum - target

        for alice in aliceSizes:
            if alice - alice_diff in bobSizes:
                return [alice, alice - alice_diff]


aliceSizes = [1,1]
bobSizes = [2,2]

aliceSizes = [1,2]
bobSizes = [2,3]

aliceSizes = [2]
bobSizes = [1,3]

solution = Solution()
print(solution.fairCandySwap(aliceSizes, bobSizes))
