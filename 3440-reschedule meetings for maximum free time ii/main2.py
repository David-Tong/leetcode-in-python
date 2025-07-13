class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        """
        :type eventTime: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        # pre-process
        startTime = [0] + startTime + [eventTime]
        endTime = [0] + endTime + [eventTime]

        L = len(startTime)
        slots = list()
        for x in range(L - 1):
            slots.append((startTime[x + 1] - endTime[x], x))
        slots = sorted(slots, key=lambda x: -x[0])
        S = len(slots)

        # helper function
        # movable - can move the meeting to another slot
        def movable(meeting, idx):
            for x in range(S):
                if meeting <= slots[x][0]:
                    if slots[x][1] not in (idx - 1, idx - 2):
                        return True
                else:
                    return False
            return False

        # process
        ans = 0
        for idx in range(2, L):
            slot = startTime[idx] - endTime[idx - 2]
            meeting = endTime[idx - 1] - startTime[idx - 1]
            ans = max(ans, slot - meeting)
            if movable(meeting, idx):
                ans = max(ans, slot)
        return ans


eventTime = 5
startTime = [1,3]
endTime = [2,5]

eventTime = 10
startTime = [0,7,9]
endTime = [1,8,10]

eventTime = 10
startTime = [0, 3, 7, 9]
endTime = [1, 4, 8, 10]

eventTime = 5
startTime = [0,1,2,3,4]
endTime = [1,2,3,4,5]

eventTime = 501828959
startTime = [_ for _ in range(1, 900000, 8)]
endTime = [_ for _ in range(4, 900004, 8) ]

solution = Solution()
print(solution.maxFreeTime(eventTime, startTime, endTime))
