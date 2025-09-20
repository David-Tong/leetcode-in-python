class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        # process
        # check "Flush"
        s = set()
        for suit in suits:
            s.add(suit)
        if len(s) == 1:
            return "Flush"

        # check "Three of a Kind"
        from collections import defaultdict
        dicts = defaultdict(int)
        for rank in ranks:
            dicts[rank] += 1
        for rank in dicts:
            if dicts[rank] > 2:
                return "Three of a Kind"

        # check "Pair"
        for rank in dicts:
            if dicts[rank] > 1:
                return "Pair"

        # check "High Card"
        return "High Card"


ranks = [13,2,3,1,9]
suits = ["a","a","a","a","a"]

ranks = [4,4,2,4,4]
suits = ["d","a","a","b","c"]

ranks = [10,10,2,12,9]
suits = ["a","b","c","a","d"]

solution = Solution()
print(solution.bestHand(ranks, suits))
