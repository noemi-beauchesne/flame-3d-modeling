"""
Aerotech motor driver (placeholder) implementing Motor interface.
Replace internals with real DLL calls later. 3.4–safe.
"""

import time
from ..core.interfaces import Motor

class AerotechMotor(Motor):
    def __init__(self, address):
        self.address = address
        self._pos = (0.0, 0.0, 0.0)
        self._connected = False

    def connect(self):
        # TODO: open DLL/session
        self._connected = True

    def home(self):
        # TODO: actual homing call
        self._pos = (0.0, 0.0, 0.0)

    def move_xyz(self, x, y, z, speed=None):
        # TODO: send motion command + wait for completion
        self._pos = (x, y, z)
        time.sleep(0.01)

    def position(self):
        return self._pos

    def is_busy(self):
        return False

    def shutdown(self):
        self._connected = False