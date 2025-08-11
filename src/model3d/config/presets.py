"""
Presets for gas ratios, standard trajectories, and default parameters.
3.4–safe: pure data + simple functions.
"""

def default_gas_ratio():
    """
    Return a dict of the default gas ratio for the flame.
    Values are fractions (sum ~ 1.0).
    """
    return {
        "argon": 0.20,
        "propane": 0.30,
        "oxygen": 0.50
    }

def default_model_name():
    """
    Return the default model name for identification in run headers.
    """
    return "baseline"

def default_visualization_params():
    """
    Example placeholder: color scale, resolution, etc.
    """
    return {
        "color_map": "jet",
        "resolution": 50
    }