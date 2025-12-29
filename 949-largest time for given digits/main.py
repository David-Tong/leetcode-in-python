class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        # pre-process
        import itertools
        arrangements = list(itertools.permutations(arr))
        arrangements = sorted(arrangements, reverse=True)
        # print(arrangements)

        # process
        # helper function
        def make(nums):
            return "".join([str(_) for _ in nums])

        def valid(arrangement):
            hour, minute = int(make(arrangement[:2])), int(make(arrangement[2:]))
            if 0 <= hour < 24 and 0 <= minute < 60:
                return True
            else:
                return False

        for arrangement in arrangements:
            if valid(arrangement):
                ans = "{}:{}".format(make(arrangement[:2]), make(arrangement[2:]))
                return ans
        return ""


arr = [1,2,3,4]
arr = [5,5,5,5]
arr = [0,4,0,0]
arr = [2,0,6,6]

solution = Solution()
print(solution.largestTimeFromDigits(arr))
