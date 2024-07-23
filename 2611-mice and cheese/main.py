class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        """
        :type reward1: List[int]
        :type reward2: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(reward1)
        diff = list()
        for x in range(L):
            diff.append((reward2[x] - reward1[x], x))
        diff = sorted(diff, key=lambda x: x[0])

        # process
        ans = 0
        for x in range(k):
            ans += reward1[diff[x][1]]
        for x in range(k, L):
            ans += reward2[diff[x][1]]
        return ans


reward1 = [1,1,3,4]
reward2 = [4,4,1,1]
k = 2

reward1 = [1,1]
reward2 = [1,1]
k = 2

reward1 = [12,16,100,46,78,9,12,3,4,5]
reward2 = [22,11,13,167,7,19,2,3,6,7]
k = 5

solution = Solution()
print(solution.miceAndCheese(reward1, reward2, k))
