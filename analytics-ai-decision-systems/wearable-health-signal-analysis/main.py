"""
Main module for the Wearable Health Signal Analysis project.

This module combines:
- cleaner.filter_nondigits() for data cleaning
- metrics (average, maximum, standard_deviation) for descriptive stats
- matplotlib for time-series visualization

It reads a phase file, cleans the data, computes key metrics, and saves a plot.
"""

from __future__ import annotations

import os
from pathlib import Path
import matplotlib.pyplot as plt

from cleaner import filter_nondigits
from metrics import average, maximum, standard_deviation


def run(filename: str):
    """
    Process heart-rate data from the specified file, clean it, calculate metrics,
    and save a visualization.

    Args:
        filename (str): Path to a phase data file (e.g., 'data/phase0.txt').

    Returns:
        tuple: (average_hr, max_hr, std_dev_hr), where each is either a float, float, float, 
        or [] if the input data is empty.
    """
    file_path = Path(filename)

    # Read raw lines from file
    with file_path.open("r", encoding="utf-8") as f:
        raw_data = f.readlines()

    # Clean data (keep only digit-only strings)
    clean_data = filter_nondigits(raw_data)

    # Compute metrics (rounding handled here for consistent output)
    avg_hr = round(average(clean_data), 2) if clean_data else []
    max_hr = round(maximum(clean_data), 2) if clean_data else []
    std_dev_hr = round(standard_deviation(clean_data), 2) if clean_data else []

    # Ensure images/ exists (relative to this script location)
    project_root = Path(__file__).resolve().parent
    images_dir = project_root / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    # Save plot with a filename based on the phase file name (prevents overwriting)
    phase_name = file_path.stem  # e.g., "phase2"
    out_path = images_dir / f"{phase_name}_hr_data.png"

    plt.plot(clean_data)
    plt.xlabel("Time (5-min intervals)")
    plt.ylabel("Heart Rate (bpm)")
    plt.title(f"Heart Rate Time Series — {phase_name}")

    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    # Manual run example
    print(run("data/phase3.txt"))
