class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.width = width
        self.height = height
        self.steps = 0
        self.perimeter = (self.width + self.height) * 2 - 4
        self.pos = [0, 0]
        self.dir = "East"

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.steps += num
        steps = self.steps % self.perimeter
        if steps == 0:
            self.pos = [0, 0]
            if self.steps > 0:
                self.dir = "South"
            else:
                self.dir = "East"
        else:
            if 0 < steps < self.width:
                self.pos = [steps, 0]
                self.dir = "East"
            else:
                steps -= self.width - 1
                if 0 < steps < self.height:
                    self.pos = [self.width - 1, steps]
                    self.dir = "North"
                else:
                    steps -= self.height - 1
                    if 0 < steps < self.width:
                        self.pos = [self.width - 1 - steps, self.height - 1]
                        self.dir = "West"
                    else:
                        steps -= self.width - 1
                        if 0 < steps < self.height:
                            self.pos = [0, self.height - 1 - steps]
                            self.dir = "South"

    def getPos(self):
        """
        :rtype: List[int]
        """
        return self.pos

    def getDir(self):
        """
        :rtype: str
        """
        return self.dir

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

robot = Robot(6, 3)
robot.step(2)
robot.step(3)
print(robot.getPos())
print(robot.getDir())
robot.step(2)
robot.step(1)
robot.step(4)
print(robot.getPos())
print(robot.getDir())
