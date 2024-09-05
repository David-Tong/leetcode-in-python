class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        L = len(asteroids)

        # pre-process
        asteroids = sorted(asteroids)
        presum = list()
        total = 0
        presum.append(total)
        for asteroid in asteroids:
            total += asteroid
            presum.append(total)

        from bisect import bisect_right
        idx = 0
        while True:
            new_idx = bisect_right(asteroids, mass)
            if new_idx == L:
                return True
            elif idx == new_idx:
                return False
            mass += presum[new_idx] - presum[idx]
            idx = new_idx


mass = 10
asteroids = [3,9,19,5,21]

mass = 5
asteroids = [4,9,23,4]

mass = 1
asteroids = [4,9,23,4]

solution = Solution()
print(solution.asteroidsDestroyed(mass, asteroids))
