
# Flame 3D Modeling

3D flame temperature modeling and acquisition system.
Designed to run hardware-controlled measurements (Aerotech stage + J-KEM thermocouple) and generate spatial temperature maps for visualization.
The codebase is Python 3.4–safe for acquisition, with optional modern visualization in a separate environment.

-----

# Features
## Hardware control
    -   Aerotech motorized stage (via ctypes/GPIB)
    -   J-KEM thermocouple temperature readings
    -   Mock hardware for offline testing
## Acquisition pipeline
    -   Configurable gas ratios, motion parameters, and trajectories
    -   Automatic run folder creation with metadata + CSV output
    -   Supports cylindrical ring and grid trajectories
## Visualization
    -   3D scatter plots and 2D XY heatmaps from recorded runs
    -   Runs in a modern Python environment for painless plotting

-----

# Project Structure

`src/model3d/`
    `core/`        # Interfaces + runner
    `config/`      # Config loader, presets
    `hardware/`    # Real & mock hardware drivers
    `modeling/`    # Coordinates, trajectories, interpolation, visualization
    `io/`          # Run/session management
    `ui/`          # CLI for acquisition & viewing
`data/`
    `raw/`         # Raw inputs (optional)
    `runs/`        # Timestamped runs with CSV + metadata
    `logs/`        # Runtime logs
`tests/`
    ...          # Unit & integration tests


-----

# Requirements

## Acquisition environment (py34-compatible-env):
    -   Python 3.6.15 (Python 3.4–compatible syntax)
    -   Minimal dependencies (no matplotlib required)
    -   Runs hardware acquisition or mock mode

## Visualization environment (viz311):
    -   Python 3.11+ recommended
    -   matplotlib, pandas for plotting

-----

# Setup

1. Clone the repo

    git clone https://github.com/yourusername/flame-3d-modeling.git
    cd flame-3d-modeling

2. Create acquisition environment

    pyenv install 3.6.15
    pyenv virtualenv 3.6.15 py34-compatible-env
    pyenv shell py34-compatible-env
    pip install -e .

3. Create visualization environment (optional)

    pyenv install 3.11.9
    pyenv virtualenv 3.11.9 viz311
    pyenv shell viz311
    pip install matplotlib pandas
    pip install -e .


-----

# Usage

## Acquisition CLI

Run in py34-compatible-env:

    python -m src.model3d.ui.cli

Prompts you through hardware prep, runs the measurement routine, and writes results to data/runs/<timestamp>/.

## Visualization CLI

Run in viz311:

    python -m src.model3d.ui.view_latest

Displays:
    -   3D scatter of temperature field
    -   2D XY heatmap at median Z

⸻

# Mock Mode

You can run the acquisition CLI without any hardware connected.
The mock mode uses placeholder drivers that:
    -   Simulate motor movement instantly
    -   Return random temperatures around 800 °C

To use mock mode:
    1. Make sure your py34-compatible-env is active
	2.	Ensure src/model3d/hardware/aerotech_controller.py and src/model3d/hardware/thermocouple_jkem.py still contain the placeholder classes provided in the repo
	3.	Run:
            python -m src.model3d.ui.cli

The program will:
    -   Generate fake coordinates from the default trajectory
    -   Record random temperatures to a CSV
    -   Save data in data/runs/<timestamp>/

You can then visualize this fake run using the visualization CLI in your viz311 environment.

-----

# Data Output

For each run:
    -   run.txt — metadata (gas ratio, model name, date/time)
    -   samples.csv — measurement points with (time, x, y, z, temp_c)

Example CSV:

    time,x,y,z,temp_c
    1723417243.123,5.0,0.0,0.0,800.54
    1723417243.321,4.9,0.87,0.0,799.32


-----

Development
    -   Code is Python 3.4–safe to allow deployment to older systems
    -   Mock hardware allows full CLI testing without physical devices
    -   Folder structure follows src/ layout with explicit package names
