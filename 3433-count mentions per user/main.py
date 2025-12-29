class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        # pre-process
        # process events
        # 0 - online event
        # 1 - offline event
        # 2 - mention ids
        # 3 - mention all
        # 4 - mention online
        happenings = list()
        for event in events:
            category, t, message = event
            t = int(t)
            if category == "OFFLINE":
                id = int(message)
                happenings.append((t, 1, id))
                happenings.append((t + 60, 0, id))
            elif category == "MESSAGE":
                if message == "ALL":
                    happenings.append((t, 3))
                elif message == "HERE":
                    happenings.append((t, 4))
                else:
                    ids = message.split()
                    happenings.append((t, 2, ids))

        # process
        happenings = sorted(happenings)
        onlines = set([_ for _ in range(numberOfUsers)])
        ans = [0] * numberOfUsers
        for happening in happenings:
            category = happening[1]
            if category == 0:
                id = happening[2]
                onlines.add(id)
            elif category == 1:
                id = happening[2]
                onlines.remove(id)
            elif category == 2:
                ids = happening[2]
                for id in ids:
                    id = int(id[2:])
                    ans[id] += 1
            elif category == 3:
                for id in range(numberOfUsers):
                    ans[id] += 1
            elif category == 4:
                for id in onlines:
                    ans[id] += 1
        return ans


numberOfUsers = 2
events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]

numberOfUsers = 2
events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]

numberOfUsers = 2
events = [["OFFLINE", "10", "0"], ["MESSAGE", "12", "HERE"]]

solution = Solution()
print(solution.countMentions(numberOfUsers, events))
