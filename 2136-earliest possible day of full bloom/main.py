class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        L = len(plantTime)

        pairs = list()
        for x in range(L):
            pairs.append((plantTime[x], growTime[x]))
        pairs = sorted(pairs, key=lambda x: (-x[1], x[0]))

        ans = 0
        offset = 0
        for plant, grow in pairs:
            ans = max(ans, offset + plant + grow)
            offset += plant
        return ans


plantTime = [1,4,3]
growTime = [2,3,1]

plantTime = [1,2,3,2]
growTime = [2,1,2,1]

plantTime = [1,10,2,3]
growTime = [10,1,8,3]

plantTime = [1]
growTime = [1]

solution = Solution()
print(solution.earliestFullBloom(plantTime, growTime))
