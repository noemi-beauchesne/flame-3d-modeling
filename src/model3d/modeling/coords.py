"""
Coordinate conversions (cartesian/cylindrical/spherical). 3.4–safe.
"""

import math

def cart_to_cyl(x, y, z):
    r = math.hypot(x, y)
    theta = math.atan2(y, x)
    return (r, theta, z)

def cyl_to_cart(r, theta, z):
    return (r * math.cos(theta), r * math.sin(theta), z)