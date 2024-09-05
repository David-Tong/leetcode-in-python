class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        from collections import deque
        queue = deque()
        for idx, ticket in enumerate(tickets):
            queue.append((idx, ticket))

        # process
        counter = 0
        while True:
            idx, ticket = queue.popleft()
            ticket -= 1
            counter += 1
            if ticket == 0 and idx == k:
                return counter
            if ticket > 0:
                queue.append((idx, ticket))


tickets = [2,3,2]
k = 2

tickets = [5,1,1,1]
k = 0

tickets = [1,1,10,10]
k = 2

solution = Solution()
print(solution.timeRequiredToBuy(tickets, k))
