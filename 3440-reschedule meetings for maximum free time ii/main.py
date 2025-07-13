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

        from collections import defaultdict
        dicts = defaultdict(set)
        L = len(startTime)
        for x in range(L - 1):
            slot = startTime[x + 1] - endTime[x]
            dicts[slot].add(x)
        slots = sorted(dicts.keys(), reverse=True)

        # helper function
        # movable - can move the meeting to another slot
        def movable(meeting, x):
            for slot in slots:
                if meeting <= slot:
                    if len(dicts[slot]) > 2:
                        return True
                    else:
                        for idx in dicts[slot]:
                            if idx not in (x - 1, x - 2):
                                return True
                else:
                    return False
            return False

        # process
        ans = 0
        for x in range(2, L):
            slot = startTime[x] - endTime[x - 2]
            meeting = endTime[x - 1] - startTime[x - 1]
            ans = max(ans, slot - meeting)
            if movable(meeting, x):
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
