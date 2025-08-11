"""
High-level Runner (3.4–safe).
Wires hardware + trajectory + I/O for a single acquisition run.
"""

import time
from .interfaces import Motor, Thermocouple
from ..io.file_io import start_run, append_sample, finish_run

class Runner(object):
    def __init__(self, motor, thermocouple, trajectory, settings):
        self.motor = motor          # Motor
        self.tc = thermocouple      # Thermocouple
        self.trajectory = trajectory
        self.settings = settings
        self.ctx = None

    def start(self):
        self.motor.connect()
        self.tc.connect()
        if self.settings.get("home_on_start", True):
            self.motor.home()
        self.ctx = start_run(self.settings)
        return self.ctx

    def execute(self, progress_cb=None):
        total = len(self.trajectory)
        idx = 0
        for (x, y, z, dwell_s) in self.trajectory:
            self.motor.move_xyz(x, y, z, speed=self.settings.get("speed"))
            time.sleep(dwell_s)
            t = self.tc.read_celsius()
            append_sample(self.ctx, time.time(), x, y, z, t)
            idx += 1
            if progress_cb:
                pct = 100.0 * float(idx) / float(total if total else 1)
                progress_cb("{}/{} {:0.1f}%".format(idx, total, pct))

    def stop(self):
        finish_run(self.ctx)
        try:
            self.tc.shutdown()
        finally:
            self.motor.shutdown()