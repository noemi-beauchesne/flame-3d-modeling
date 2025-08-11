"""
Find the most recent data/runs/<timestamp>/ and show quick plots.
Usage:
    python -m src.model3d.ui.view_latest
"""

import os
import glob
from ..config.loader import load_settings
from ..modeling.visualization import load_samples, plot_scatter3d, plot_xy_heatmap

def _latest_run_folder(runs_root):
    # Find the newest directory by mtime
    candidates = [d for d in glob.glob(os.path.join(runs_root, "*")) if os.path.isdir(d)]
    if not candidates:
        return None
    candidates.sort(key=lambda p: os.path.getmtime(p), reverse=True)
    return candidates[0]

def main():
    settings = load_settings()
    data_root = settings.get("output_root")
    runs_root = os.path.join(data_root, "runs")
    folder = _latest_run_folder(runs_root)
    if not folder:
        print("No runs found in: " + runs_root)
        return
    csv_path = os.path.join(folder, "samples.csv")
    if not os.path.exists(csv_path):
        print("No samples.csv found in: " + folder)
        return

    print("Loading: " + csv_path)
    samples = load_samples(csv_path)

    # 3D scatter
    plot_scatter3d(samples)

    # 2D heatmap on XY (nearest neighbor)
    plot_xy_heatmap(samples, nx=50, ny=50)

if __name__ == "__main__":
    main()