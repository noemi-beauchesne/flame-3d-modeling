"""
Minimal plotting helpers (3.4–safe).
- load_samples(csv_path) -> list of (x,y,z,t)
- plot_scatter3d(samples): 3D scatter of points colored by temperature
- plot_xy_heatmap(samples, nx, ny): 2D XY heatmap (nearest-neighbor binning)
"""

import csv
import math

def load_samples(csv_path):
    samples = []
    with open(csv_path, "r") as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            x = float(row["x"]); y = float(row["y"]); z = float(row["z"]); t = float(row["temp_c"])
            samples.append((x, y, z, t))
    return samples

def plot_scatter3d(samples):
    # Lazy import so module works even if matplotlib is missing
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed to enable 3D)

    xs = [p[0] for p in samples]
    ys = [p[1] for p in samples]
    zs = [p[2] for p in samples]
    ts = [p[3] for p in samples]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(xs, ys, zs, c=ts)  # no explicit colors (policy)
    cb = fig.colorbar(sc)
    cb.set_label("Temp (°C)")
    ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
    ax.set_title("3D Scatter: Temperature")
    plt.show()

def plot_xy_heatmap(samples, nx, ny):
    """
    Simple nearest-neighbor binning onto an XY grid at median Z.
    """
    import matplotlib.pyplot as plt
    import numpy as np

    xs = [p[0] for p in samples]
    ys = [p[1] for p in samples]
    zs = [p[2] for p in samples]
    ts = [p[3] for p in samples]

    z_sorted = sorted(zs)
    z_med = z_sorted[len(z_sorted)//2] if z_sorted else 0.0

    # Choose only points closest to median Z (within tolerance)
    tol = 1e-6
    pts = [(x, y, t) for (x, y, z, t) in samples if abs(z - z_med) <= tol]

    if not pts:
        # fallback: use all points (projected)
        pts = [(x, y, t) for (x, y, z, t) in samples]

    xs2 = [p[0] for p in pts]; ys2 = [p[1] for p in pts]; ts2 = [p[2] for p in pts]
    x_min, x_max = min(xs2), max(xs2)
    y_min, y_max = min(ys2), max(ys2)

    gx = np.linspace(x_min, x_max, nx)
    gy = np.linspace(y_min, y_max, ny)
    grid = np.zeros((ny, nx))

    # Nearest-neighbor fill
    for j in range(ny):
        for i in range(nx):
            xq = gx[i]; yq = gy[j]
            best = 1e99; val = 0.0
            for (x, y, t) in pts:
                d = (x - xq)*(x - xq) + (y - yq)*(y - yq)
                if d < best:
                    best = d; val = t
            grid[j, i] = val

    plt.figure()
    im = plt.imshow(grid, origin="lower",
                    extent=[x_min, x_max, y_min, y_max],
                    aspect="auto")
    cb = plt.colorbar(im)
    cb.set_label("Temp (°C)")
    plt.xlabel("X"); plt.ylabel("Y")
    plt.title("XY Heatmap (nearest neighbor)")
    plt.show()