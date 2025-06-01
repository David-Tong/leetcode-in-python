class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for answer in answers:
            dicts[answer] += 1

        # process
        ans = 0
        for answer in dicts:
            count = 0
            if dicts[answer] % (answer + 1) != 0:
                count += 1
            ans += (dicts[answer] // (answer + 1) + count) * (answer + 1)
        return ans


answers = [1,1,2]
answers = [10,10,10]
answers = [1,1,1,3]

solution = Solution()
print(solution.numRabbits(answers))
