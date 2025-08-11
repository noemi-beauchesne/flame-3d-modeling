"""
Creates data/runs/<timestamp>/, writes meta header and CSV samples. 3.4–safe.
"""

import os
import time
import csv

class RunContext(object):
    def __init__(self, root, folder, csv_path, meta_path, start_ts, settings):
        self.root = root
        self.folder = folder
        self.csv_path = csv_path
        self.meta_path = meta_path
        self.start_ts = start_ts
        self.settings = settings
        self._csv_file = None
        self._writer = None

def _ensure_dirs(root):
    for sub in ("runs", "logs"):
        p = os.path.join(root, sub)
        if not os.path.isdir(p):
            os.makedirs(p)
    return os.path.join(root, "runs")

def start_run(settings):
    root = settings.get("output_root", os.path.abspath(os.path.join(os.getcwd(), "data")))
    runs_root = _ensure_dirs(root)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    folder = os.path.join(runs_root, stamp)
    os.makedirs(folder)

    csv_path = os.path.join(folder, "samples.csv")
    meta_path = os.path.join(folder, "run.txt")

    ctx = RunContext(root, folder, csv_path, meta_path, time.time(), settings)

    # meta/header
    ratios = settings.get("gas_ratio", {})
    with open(meta_path, "w") as f:
        f.write("Ratio Ag:{:.2f} Pr:{:.2f} O2:{:.2f} | model:{}\n".format(
            ratios.get("argon", 0.0), ratios.get("propane", 0.0), ratios.get("oxygen", 0.0),
            settings.get("model_name", "unknown")
        ))
        f.write("date:{} | start:{} | est:unknown | end:pending\n".format(
            time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S")
        ))

    # csv
    ctx._csv_file = open(csv_path, "w", newline="")
    ctx._writer = csv.writer(ctx._csv_file)
    ctx._writer.writerow(["time", "x", "y", "z", "temp_c"])

    return ctx

def append_sample(ctx, t, x, y, z, temp_c):
    ctx._writer.writerow([t, x, y, z, temp_c])
    ctx._csv_file.flush()

def finish_run(ctx):
    try:
        if ctx and ctx._csv_file:
            ctx._csv_file.flush()
            ctx._csv_file.close()
    finally:
        with open(ctx.meta_path, "a") as f:
            f.write("\nend:{} | actual:{}s\n".format(
                time.strftime("%H:%M:%S"), int(time.time() - ctx.start_ts)
            ))