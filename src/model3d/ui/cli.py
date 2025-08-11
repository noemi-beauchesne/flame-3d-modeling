"""
Simple interactive CLI to drive a mock acquisition. 3.4–safe.
"""

# At the very top of src/model3d/ui/cli.py
try:
    input = raw_input  # Python 2
except NameError:
    pass  # Python 3 already has input()


from ..config.loader import load_settings
from ..hardware.aerotech_controller import AerotechMotor
from ..hardware.thermocouple_jkem import JKEMThermocouple
from ..modeling.trajectory import CylindricalRing
from ..core.run import Runner

def main():
    print("=== 3D Modeling CLI (3.4–safe) ===")
    input("1) Push motor (press Enter when done)")
    input("2) D/G motor (press Enter when done)")

    settings = load_settings()

    motor = AerotechMotor(settings["gpib_address"])
    tc = JKEMThermocouple(settings["jk_port"])

    # 36 points around a ring at z = 0
    thetas = [i * 3.1415926535 / 18.0 for i in range(36)]
    traj = CylindricalRing(r=5.0, thetas=thetas, z=0.0, dwell_s=settings["dwell_seconds"])

    runner = Runner(motor, tc, traj, settings)
    runner.start()
    print("Initializing... complete!")
    input("Open gas and light flame, then press Enter")

    print("Running...")
    runner.execute(progress_cb=lambda s: print("> " + s))
    runner.stop()
    print("Done. Check data/runs/ for outputs.")

if __name__ == "__main__":
    main()