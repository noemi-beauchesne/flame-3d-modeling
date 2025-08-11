"""
Trajectory generators — yield (x, y, z, dwell_seconds). 3.4–safe.
"""

from .coords import cyl_to_cart

class Trajectory(object):
    def __len__(self):
        return 0
    def __iter__(self):
        return iter(())

class CylindricalRing(Trajectory):
    def __init__(self, r, thetas, z, dwell_s):
        self._points = []
        for th in thetas:
            x, y, zc = cyl_to_cart(r, th, z)
            self._points.append((x, y, zc, dwell_s))

    def __len__(self):
        return len(self._points)

    def __iter__(self):
        return iter(self._points)