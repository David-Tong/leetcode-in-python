class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        def getTeamLen(team):
            if team == 0:
                return float("inf")
            ans = 0
            while team:
                if team & 1:
                    ans += 1
                team >>= 1
            return ans

        def convertToTeam(team_mask):
            ans = list()
            idx = 0
            while team_mask:
                if team_mask & 1:
                    ans.append(idx)
                team_mask >>= 1
                idx += 1
            return ans

        # pre-process
        from collections import defaultdict
        skills = defaultdict(int)

        for idx, req_skill in enumerate(req_skills):
            skills[req_skill] = idx
        L = len(skills)

        req_mask = 0
        for req_skill in req_skills:
            req_mask |= 1 << skills[req_skill]

        people_masks = list()
        for ppl in people:
            people_mask = 0
            for skill in ppl:
                if skill in skills:
                    people_mask |= 1 << skills[skill]
            people_masks.append(people_mask)

        # knapsack dp
        N = len(people)

        from copy import deepcopy
        from collections import defaultdict
        prev_dp = defaultdict(long)
        prev_dp[0] = (0)

        ans = -1
        for idx, people_mask in enumerate(people_masks):
            if people_mask != 0:
                dp = deepcopy(prev_dp)
                masks = prev_dp.keys()
                for mask in masks:
                    new_mask = mask | people_mask
                    new_team = prev_dp[mask] | 1 << idx
                    if getTeamLen(new_team) < getTeamLen(prev_dp[new_team]):
                        if getTeamLen(new_team) <= getTeamLen( dp[new_mask]):
                            dp[new_mask] = new_team
                prev_dp = dp

        ans = convertToTeam(dp[req_mask])
        return ans


req_skills = ["java","nodejs","reactjs"]
people = [["java"],["nodejs"],["nodejs","reactjs"]]

req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]

req_skills = ["hkyodbbhr","p","biflxurxdvb","x","qq","yhiwcn"]
people = [["yhiwcn"],[],[],[],["biflxurxdvb","yhiwcn"],["hkyodbbhr"],["hkyodbbhr","p"],["hkyodbbhr"],[],["yhiwcn"],["hkyodbbhr","qq"],["qq"],["hkyodbbhr"],["yhiwcn"],[],["biflxurxdvb"],[],["hkyodbbhr"],["hkyodbbhr","yhiwcn"],["yhiwcn"],["hkyodbbhr"],["hkyodbbhr","p"],[],[],["hkyodbbhr"],["biflxurxdvb"],["qq","yhiwcn"],["hkyodbbhr","yhiwcn"],["hkyodbbhr"],[],[],["hkyodbbhr"],[],["yhiwcn"],[],["hkyodbbhr"],["yhiwcn"],["yhiwcn"],[],[],["hkyodbbhr","yhiwcn"],["yhiwcn"],["yhiwcn"],[],[],[],["yhiwcn"],[],["yhiwcn"],["x"],["hkyodbbhr"],[],[],["yhiwcn"],[],["biflxurxdvb"],[],[],["hkyodbbhr","biflxurxdvb","yhiwcn"],[]]

"""
req_skills = ["a", "b"]

from random import randint
people = list()
for x in range(60):
    skills = set()
    for y in range(randint(0, 15)):
        skills.add(chr(ord('a') + randint(0, 15)))
    people.append(list(skills))

print(req_skills)
print(people)
"""

solution = Solution()
print(solution.smallestSufficientTeam(req_skills, people))
