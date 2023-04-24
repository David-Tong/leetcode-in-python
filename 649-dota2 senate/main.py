class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        from collections import deque
        queue = deque()

        radiant_bans = 0
        dire_bans = 0
        for snt in senate:
            queue.append(snt)

        while queue:
            finish = True
            for item in queue:
                if item != queue[0]:
                    finish = False
                    break
            if finish:
                if queue[0] == 'R':
                    return 'Radiant'
                elif queue[0] == 'D':
                    return 'Dire'

            snt = queue.popleft()
            if snt == 'R':
                if dire_bans > 0:
                    dire_bans -= 1
                else:
                    radiant_bans += 1
                    queue.append(snt)
            elif snt == 'D':
                if radiant_bans > 0:
                    radiant_bans -= 1
                else:
                    dire_bans += 1
                    queue.append(snt)


senate = "RD"
senate = "RDD"
#senate = "RDDDRDRRRRRRDDRDRRRD"
#senate = "R"
#senate = "RRRRRRRR"
#senate = "DDDRRRR"
#senate = "DDRRR"
#senate = "DRDRR"

solution = Solution()
print(solution.predictPartyVictory(senate))
