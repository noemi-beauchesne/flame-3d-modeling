"""
Abstract interfaces for hardware (3.4–safe).
We avoid typing/Protocol; use simple base classes with NotImplementedError.
"""

class Motor(object):
    def connect(self):
        raise NotImplementedError
    def home(self):
        raise NotImplementedError
    def move_xyz(self, x, y, z, speed=None):
        raise NotImplementedError
    def position(self):
        raise NotImplementedError
    def is_busy(self):
        raise NotImplementedError
    def shutdown(self):
        raise NotImplementedError

class Thermocouple(object):
    def connect(self):
        raise NotImplementedError
    def read_celsius(self):
        raise NotImplementedError
    def shutdown(self):
        raise NotImplementedError