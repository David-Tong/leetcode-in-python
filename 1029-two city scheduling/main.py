class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        N = len(costs) // 2

        ans = 0
        refunds = []
        for cost in costs:
            ans += cost[0]
            refunds.append(cost[1] - cost[0])

        refunds = sorted(refunds)
        ans += sum(refunds[0:N])

        return ans

costs = [[10,20],[30,200],[400,50],[30,20]]
#costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
#costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]

costs = [[403,578],[406,455],[710,697],[155,861],[540,843],[911,753],[477,453],[378,936],[492,720],[915,382],[984,200],[449,448],[525,964],[875,767],[905,753],[18,84],[351,167],[554,582],[175,794],[677,301],[268,994],[631,627],[53,107],[995,390],[540,406],[932,808],[426,455],[997,735],[449,757],[90,869],[640,396],[573,536]]

solution = Solution()
print(solution.twoCitySchedCost(costs))