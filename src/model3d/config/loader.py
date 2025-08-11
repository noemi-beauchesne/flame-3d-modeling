"""
Loads settings from config.ini (if present) with sane defaults.
3.4–safe: no f-strings, no typing.
"""

import os
import configparser
from . import presets

def load_settings(path=None):
    cfg = configparser.ConfigParser()
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "config.ini")
    if os.path.exists(path):
        cfg.read(path)

    settings = {}

    # Hardware
    settings["gpib_address"] = cfg.get("hardware", "gpib_address", fallback="GPIB0::1::INSTR")
    settings["jk_port"] = cfg.get("hardware", "jk_port", fallback="COM3")
    settings["home_on_start"] = cfg.getboolean("hardware", "home_on_start", fallback=True)

    # Acquisition
    settings["speed"] = cfg.getfloat("acquisition", "speed", fallback=5.0)
    settings["dwell_seconds"] = cfg.getfloat("acquisition", "dwell_seconds", fallback=0.2)

    # Paths
    default_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "data"))
    settings["output_root"] = cfg.get("paths", "output_root", fallback=default_root)

    # Presets (can be overridden later)
    settings["gas_ratio"] = presets.default_gas_ratio()
    settings["model_name"] = presets.default_model_name()

    return settings