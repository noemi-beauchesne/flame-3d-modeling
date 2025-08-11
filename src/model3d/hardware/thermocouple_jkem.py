"""
J-KEM thermocouple driver (placeholder). 3.4–safe.
Replace with real serial/GPIB I/O later.
"""

import random
from ..core.interfaces import Thermocouple

class JKEMThermocouple(Thermocouple):
    def __init__(self, port):
        self.port = port
        self._connected = False

    def connect(self):
        # TODO: open serial
        self._connected = True

    def read_celsius(self):
        # TODO: read from device
        return 800.0 + random.uniform(-2.0, 2.0)

    def shutdown(self):
        self._connected = False