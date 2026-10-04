class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # pre-process
        L = len(stones)
        counts = [0] * 3
        for stone in stones:
            mod = stone % 3
            counts[mod] += 1

        # helper function
        # a sequence can keep game must run must be like below
        # take start from 1 for example, but you may replace it with 2 same as
        # 1 + 1 2 1 2 1 2 [used up all 1 and 2 pairs] + 1 + 0 0 0 0 0 [used up all 0s]
        def check(zeros, ones, twos):
            # only 2, Alice must lost
            if ones == 0:
                return False
            # start the sequence
            ones -= 1
            rounds = 1 + min(ones, twos) * 2 + zeros
            if ones > twos:
                rounds += 1
            return rounds < L and rounds % 2 != 0

        # process
        ans = check(counts[0], counts[1], counts[2]) or check(counts[0], counts[2], counts[1])
        return ans


stones = [2,1]
"""
stones = [2]
stones = [5,1,2,4,3]
stones = [19,2,17,20,7,17]
stones = [2,2,3]
stones = [2,2,1]
stones = [20,3,20,17,2,12,15,17,4]
stones = [15,20,10,13,14,15,5,2,3]
"""

solution = Solution()
print(solution.stoneGameIX(stones))
