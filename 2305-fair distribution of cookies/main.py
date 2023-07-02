class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        L = len(cookies)

        def getUnfairness(dist):
            children = [0] * k
            for idx, child in enumerate(dist):
                child = int(child)
                children[child] += cookies[idx]
            return max(children)

        def distribute(dist):
            if len(dist) == L:
                return getUnfairness(dist)

            # prune
            from collections import defaultdict
            children = defaultdict(int)
            for child in dist:
                children[child] = True

            if L - len(dist) <= k - len(children.keys()):
                for x in range(k):
                    if str(x) not in children:
                        dist += str(x)
                return getUnfairness(dist)
            else:
                ans = float("inf")
                for child in range(k):
                    ans = min(ans, distribute(dist + str(child)))
            return ans

        return distribute("")


cookies = [8,15,10,20,8]
k = 2

cookies = [6,1,3,2,2,4,1,2]
k = 3

cookies = [6,1,3,2,2,4,1,2]
k = 6

cookies = [6,1,3,2,2,4,1,2]
k = 8

cookies = [6,1,3,2,2,4,1,2]
k = 5

solution = Solution()
print(solution.distributeCookies(cookies, k))
