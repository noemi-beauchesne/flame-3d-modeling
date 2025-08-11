"""
Wraps interpolation to provide a callable temperature field T(x,y,z).
"""

class TemperatureField(object):
    def __init__(self, samples, method="nearest"):
        self.samples = samples
        self.method = method

    def __call__(self, x, y, z):
        from .interpolation import nearest_neighbor
        if self.method == "nearest":
            return nearest_neighbor(self.samples, (x, y, z))
        raise ValueError("unknown method {}".format(self.method))