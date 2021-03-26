import math


class Center:
    def __init__(self, x_coord: int or float, y_coord: int or float):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __str__(self):
        return f'Center is x={self.x_coord}, y={self.y_coord}'


class Disc:
    def __init__(self, center: Center, radius: int):
        self.center = (center.x_coord, center.y_coord)
        self.radius = radius

    def __str__(self):
        if self.center[0] == 0:
            x_coord = ''
        else:
            x_coord = '-' if self.center[0] >= 0 else '+'
            x_coord += '{:.2f}'.format(abs(self.center[0]))

        if self.center[1] == 0:
            y_coord = ''
        else:
            y_coord = '-' if self.center[1] > 0 else '+'
            y_coord += '{:.2f}'.format(abs(self.center[1]))

        radius = '{:.2f}'.format(self.radius ** 2)
        return f'(x{x_coord})**2 + (y{y_coord})**2 = {radius}'

    def is_touching(self, other: object, precision: int):
        distance = ((self.center[0] - other.center[0]) ** 2 +
                    (self.center[1] - other.center[1]) ** 2) ** 0.5
        distance = round(distance, precision)
        res = False
        return distance == round(self.radius + other.radius) or\
               distance == round(abs(self.radius - other.radius))

    def inscribe_discs(self):
        radius = self.radius / 2
        y_coord = self.center[1]
        x_coord_1 = self.center[0] - radius
        x_coord_2 = self.center[0] + radius
        disk1 = Disc(Center(x_coord_1, y_coord), radius)
        disk2 = Disc(Center(x_coord_2, y_coord), radius)
        return disk1, disk2

    def transform_disc(self, radius_difference):
        self.radius += radius_difference

    def transformed_disc(self, radius_difference):
        return Disc(Center(*self.center), self.radius+radius_difference)

    def __eq__(self, other):
        if isinstance(other, Disc):
            res = self.center == other.center and self.radius == other.radius
        else:
            res = False
        return res

    def __hash__(self):
        return hash((self.center, self.radius))

    @staticmethod
    def fromstring(string):
        x_coord, y_coord, radius = map(int, string.split(' '))
        return Disc(Center(x_coord, y_coord), radius)
