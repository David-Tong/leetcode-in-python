class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def isValid(image, x, y, changeColor):
            if x < 0 or x >= len(image) \
                or y < 0 or y >= len(image[0]):
                return False
            else:
                if image[x][y] != changeColor:
                    return False
                else:
                    return True

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        bfs = []
        bfs.append((sr, sc))
        visited = []
        visited.append((sr, sc))
        changeColor = image[sr][sc]
        while len(bfs) > 0:
            (x, y) = bfs.pop(0)
            image[x][y] = newColor
            visited.append((x, y))
            for (delta_x, delta_y) in directions:
                next_x = x + delta_x
                next_y = y + delta_y
                if (next_x, next_y) not in visited:
                    if isValid(image, next_x, next_y, changeColor):
                        bfs.append((next_x, next_y))
                        visited.append((next_x, next_y))
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2

image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
newColor = 2

solution = Solution()
print(solution.floodFill(image, sr, sc, newColor))
