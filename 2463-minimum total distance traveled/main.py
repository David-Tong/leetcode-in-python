class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(robot)
        N = len(factory)
        robot = sorted(robot)
        factory = sorted(factory)

        # calculate the distance for robot 0 to N - 1 to travel to factory M - 1
        # distances[x][y][z] - the total distance for robots y to z to travel to factory x
        distances = [[[0] * M for _ in range(M)] for _ in range(N)]
        for x in range(N):
            for y in range(M):
                distance = 0
                for z in range(y, M):
                    distance += abs(robot[z] - factory[x][0])
                    distances[x][y][z] = distance
        # print(distances)

        # process
        # dp init
        # dp[x][y] - the minimal total distance travelled to get 0 to y robots repaired in the 0 to x factories
        dp = [[float("inf")] * (M + 1) for _ in range(N)]
        # dp[x][0] - no robots assigned to 0 to x factory, should be 0
        for x in range(N):
            dp[x][0] = 0
        for y in range(factory[0][1]):
            dp[0][y + 1] = distances[0][0][y]
        # print(dp)

        # dp transfer
        for x in range(1, N):
            for y in range(1, M + 1):
                dp[x][y] = dp[x - 1][y]
                for z in range(factory[x][1]):
                    if y - z > 0:
                        dp[x][y] = min(dp[x][y], dp[x - 1][y - z - 1] + distances[x][y - z - 1][y - 1])
        # print(dp)
        return dp[N - 1][M]


robot = [0,4,6]
factory = [[2,2],[6,2]]

robot = [1,-1]
factory = [[-2,1],[2,1]]

robot = [-5,-10,3,4,5,6,78,9]
factory = [[0,4],[10,5],[25,4]]

robot = [789300819,-600989788,529140594,-592135328,-840831288,209726656,-671200998]
factory = [[-865262624,6],[-717666169,0],[725929046,2],[449443632,3],[-912630111,0],[270903707,3],[-769206598,2],[-299780916,4],[-159433745,5],[-467185764,3],[849991650,7],[-292158515,6],[940410553,6],[258278787,0],[83034539,2],[54441577,3],[-235385712,2],[75791769,3]]

solution = Solution()
print(solution.minimumTotalDistance(robot, factory))
