class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        idx = 1
        ans = list()
        for num in target:
            while idx < num:
                ans.append("Push")
                ans.append("Pop")
                idx += 1
            ans.append("Push")
            idx += 1
        return ans


target = [1,3]
n = 3

target = [1,2,3]
n = 3

target = [1,2]
n = 4

target = [1,3,5,7,10]
n = 11

solution = Solution()
print(solution.buildArray(target, n))
