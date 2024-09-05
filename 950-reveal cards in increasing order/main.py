class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(deck)
        idxes = [_ for _ in range(L)]
        deck = sorted(deck)

        # simulation
        from collections import deque
        queue = deque()

        for idx in idxes:
            queue.append(idx)

        cards = list()
        while queue:
            idx = queue.popleft()
            cards.append(idx)
            if queue:
                queue.append(queue.popleft())

        # answer
        ans = [0] * L
        for idx, card in enumerate(cards):
            ans[card] = deck[idx]
        return ans


deck = [17,13,11,2,3,5,7]
deck = [1,1000]
deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

solution = Solution()
print(solution.deckRevealedIncreasing(deck))
