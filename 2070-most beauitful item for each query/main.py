class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(items)
        items = sorted(items, key=lambda x: (x[0], x[1]))
        sorted_queries = sorted(queries)

        # process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        idx = 0
        from collections import defaultdict
        beautifuls = defaultdict(int)
        for query in sorted_queries:
            while idx < L and items[idx][0] <= query:
                heappush(heap, -items[idx][1])
                idx += 1
            if heap:
                beautifuls[query] = -heap[0]
            else:
                beautifuls[query] = 0

        # post-process
        ans = list()
        for query in queries:
            ans.append(beautifuls[query])
        return ans


items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]

items = [[1,2],[1,2],[1,3],[1,4]]
queries = [1]

items = [[10,1000]]
queries = [5]

items = [[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]]
queries = [885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]

solution = Solution()
print(solution.maximumBeauty(items, queries))
