class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # pre-process
        L = len(nums)
        odds_odds= [0] * L
        odds_evens = [0] * L
        evens_odds = [0] * L
        evens_evens = [0] * L

        for x in range(L):
            if x % 2 == 0:
                if nums[x] % 2 == 0:
                    evens_evens[x] = 1
                else:
                    evens_odds[x] = 1
            else:
                if nums[x] % 2 == 0:
                    odds_evens[x] = 1
                else:
                    odds_odds[x] = 1
        #print(odds_odds)
        #print(odds_evens)
        #print(evens_odds)
        #print(evens_evens)

        odds_odds_presum = [0]
        for odd_odd in odds_odds:
            odds_odds_presum.append(odds_odds_presum[-1] + odd_odd)
        odds_evens_presum = [0]
        for odd_even in odds_evens:
            odds_evens_presum.append(odds_evens_presum[-1] + odd_even)
        evens_odds_presum = [0]
        for even_odd in evens_odds:
            evens_odds_presum.append(evens_odds_presum[-1] + even_odd)
        evens_evens_presum = [0]
        for even_even in evens_evens:
            evens_evens_presum.append(evens_evens_presum[-1] + even_even)
        #print(odds_odds_presum)
        #print(odds_evens_presum)
        #print(evens_odds_presum)
        #print(evens_evens_presum)

        # process
        # helper function
        # presums - suppose to have evens only
        # presums2 - suppose to have odds only
        def check(start, end, presums, presums2):
            if presums[end + 1] - presums[start] != 0:
                return False
            else:
                if presums2[end + 1] - presums2[start] != 0:
                    return False
                else:
                    return True

        ans = list()
        for query in queries:
            start, end = query
            if nums[start] % 2 == 0:
                if start % 2 == 0:
                    # evens should be even only, odds should be odd only
                    ans.append(check(start, end, evens_odds_presum, odds_evens_presum))
                else:
                    # odds should be even only, evens should be odd only
                    ans.append(check(start, end, odds_odds_presum, evens_evens_presum))
            else:
                if start % 2 == 0:
                    # evens should be odd only, odds should be even only
                    ans.append(check(start, end, odds_odds_presum, evens_evens_presum))
                else:
                    # odds should be odd only, evens should even only
                    ans.append(check(start, end, evens_odds_presum, odds_evens_presum))
        return ans


nums = [3,4,1,2,6]
queries = [[0,4]]

nums = [4,3,1,6]
queries = [[0,2],[2,3]]

nums = [4,3,1,7,8,5,9,11,10,12,13,14]
queries = [[0,2],[2,3],[3,5],[3,6],[7,10]]


solution = Solution()
print(solution.isArraySpecial(nums, queries))
