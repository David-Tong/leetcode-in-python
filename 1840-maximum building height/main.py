class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        # pre-process
        # we assume input: n (int), restrictions (list of [id, maxH])
        # we will sort restrictions, add [1,0], add [n, inf], then propagate limits.
        # add building 1 restriction
        restrictions.append([1, 0])
        # add building n with infinite height
        restrictions.append([n, float("inf")])

        # sort by building id
        restrictions.sort()

        # from left to right
        # ensure each restriction respects the previous one
        for x in range(1, len(restrictions)):
            prev_id, prev_h = restrictions[x - 1]
            cur_id, cur_h = restrictions[x]

            dist = cur_id - prev_id
            # max height allowed from left neighbor
            allowed = prev_h + dist
            # keep the smaller one
            restrictions[x][1] = min(cur_h, allowed)

        # from right to left
        # ensure each restriction respects the next one
        for x in range(len(restrictions) - 2, -1, -1):
            next_id, next_h = restrictions[x + 1]
            cur_id, cur_h = restrictions[x]

            dist = next_id - cur_id
            # max height allowed from right neighbor
            allowed = next_h + dist
            # keep the smaller one
            restrictions[x][1] = min(cur_h, allowed)

        # process
        # now compute the maximum possible peak between restrictions
        ans = 0
        for x in range(1, len(restrictions)):
            left_id, left_h = restrictions[x - 1]
            right_id, right_h = restrictions[x]

            dist = right_id - left_id

            # the highest peak between two restrictions is:
            # (left_h + right_h + dist) // 2
            # this comes from two slopes rising and falling by 1 per step.
            peak = (left_h + right_h + dist) // 2
            ans = max(ans, peak)

        return ans


n = 5
restrictions = [[2,1],[4,1]]

n = 6
restrictions = []

n = 10
restrictions = [[5,3],[2,5],[7,4],[10,3]]

import random
def generate_test_data():
    # maximum n
    n = 10**9

    # maximum number of restrictions
    max_r = min(n - 1, 10**5)

    # random number of restrictions (could also force max_r)
    r = max_r

    # generate unique building IDs in [2, n]
    ids = random.sample(xrange(2, n + 1), r)

    restrictions = []
    for idi in ids:
        maxH = random.randint(0, 10**9)
        restrictions.append([idi, maxH])

    # Sort for readability (optional)
    restrictions.sort()

    return n, restrictions

n, restrictions = generate_test_data()

print(n)
print(restrictions)

solution = Solution()
print(solution.maxBuilding(n, restrictions))
