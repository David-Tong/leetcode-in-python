class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        # pre-process
        if len(hand) % groupSize != 0:
            return False

        N = len(hand) // groupSize

        from collections import defaultdict
        dicts = defaultdict(int)

        for hnd in hand:
            dicts[hnd] += 1

        # process
        for _ in range(N):
            start = min(dicts.keys())
            for x in range(groupSize):
                if start + x in dicts:
                    dicts[start + x] -= 1
                    if dicts[start + x] == 0:
                        del dicts[start + x]
                else:
                    return False
        return True


hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3

hand = [1,2,3,4,5]
groupSize = 4

hand = [1,2,2,3,3,4,4,5]
groupSize = 2

solution = Solution()
print(solution.isNStraightHand(hand, groupSize))
