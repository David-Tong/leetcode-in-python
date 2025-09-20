class Solution(object):
    def shiftDistance(self, s, t, nextCost, previousCost):
        """
        :type s: str
        :type t: str
        :type nextCost: List[int]
        :type previousCost: List[int]
        :rtype: int
        """
        # pre-process
        L = len(s)
        C = 26
        next_presum = [0]
        for nc in nextCost:
            next_presum.append(next_presum[-1] + nc)
        previous_presum = [0]
        for pc in previousCost:
            previous_presum.append(previous_presum[-1] + pc)

        # helper function
        # cost - the minimum cost to transfer ch to ch2
        from collections import defaultdict
        cache = defaultdict(int)
        def cost(ch, ch2):
            key = "{}-{}".format(ch, ch2)
            if key in cache:
                return cache[key]

            res = float("inf")
            idx, idx2 = ord(ch) - ord('a'), ord(ch2) - ord('a')
            if idx == idx2:
                return 0

            # case 1, ch shift to next letter to reach ch2
            # case 1.1, ch is smaller than or equal to ch2
            if idx < idx2:
                res = min(res, next_presum[idx2] - next_presum[idx])
            # case 1.2, ch is larger than ch2
            else:
                res = min(res, next_presum[C] - next_presum[idx] + next_presum[idx2])

            # case 2, ch shift to the previous letter to reach ch2
            if idx > idx2:
                res = min(res, previous_presum[idx + 1] - previous_presum[idx2 + 1])
            else:
                res = min(res, previous_presum[idx + 1] + previous_presum[C] - previous_presum[idx2 + 1])

            cache[key] = res
            return res

        # process
        ans = 0
        for x in range(L):
            ans += cost(s[x], t[x])
        return ans


s = "abab"
t = "baba"
nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

s = "leet"
t = "code"
nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

solution = Solution()
print(solution.shiftDistance(s, t, nextCost, previousCost))
