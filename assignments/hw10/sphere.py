# represents a geometric solid sphere

from math import pi


class Sphere:
    def __init__(self, radius):
        self.radius = radius
        self.volume = 0
        self.surface_area = 0

    def get_radius(self):
        return self.radius

    def surface_area(self):
        self.surface_area = 4 * pi * (self.radius ** 2)
        return self.surface_area

    def volume(self):
        sec_radius = self.radius
        cubic_r = sec_radius ** 3
        self.volume = (4/3) * pi * cubic_r
        return self.volume
