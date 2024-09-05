class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        has = [False] * 3
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            for x in range(3):
                if triplet[x] == target[x]:
                    has[x] = True

            ans = True
            for x in range(3):
                ans &= has[x]
            if ans:
                return ans
        return False


triplets = [[2,5,3],[1,8,4],[1,7,5]]
target = [2,7,5]

triplets = [[3,4,5],[4,5,6]]
target = [3,2,5]

triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
target = [5,5,5]

solution = Solution()
print(solution.mergeTriplets(triplets, target))
