class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1:
            if self.big > 0:
                self.big -= 1
            else:
                return False
        elif carType == 2:
            if self.medium > 0:
                self.medium -= 1
            else:
                return False
        elif carType == 3:
            if self.small > 0:
                self.small -= 1
            else:
                return False
        return True


parkingsystem = ParkingSystem(1, 1, 0)
print(parkingsystem.addCar(1))
print(parkingsystem.addCar(2))
print(parkingsystem.addCar(3))
print(parkingsystem.addCar(1))
