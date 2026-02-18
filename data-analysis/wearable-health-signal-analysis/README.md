# Wearable Health Signal Analysis

**Fari Lindo • DataInsideData™**

**Role:** Data Analyst (Portfolio Project)

Data Analyst Health-Tech Case Study | Time-Series Behavioral Inference |Python

## Tech Stack

![Python](https://img.shields.io/badge/Python-000000?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-000000?logo=jupyter&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)

---

![Last Commit](https://img.shields.io/github/last-commit/dataeden/fari-tech-portfolio)
![Repo Size](https://img.shields.io/github/repo-size/dataeden/fari-tech-portfolio)
![Top Language](https://img.shields.io/github/languages/top/dataeden/fari-tech-portfolio)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Executive Summary

This project analyzes multi-phase heart-rate telemetry collected from a
wearable device sampling every 5 minutes over an 8-hour period.

The objective is to:

-   Clean noisy physiological signal data
-   Remove non-numeric and corrupted entries
-   Compute descriptive statistics
-   Infer behavioral states (sleep, exercise, awake activity)
-   Prototype logic for future sleep-quality scoring models

The system is built using modular Python components and test-driven
development principles to ensure analytical integrity.

------------------------------------------------------------------------

## Dataset Overview

-   4 time-series data files (`phase0–phase3`)
-   Sampling interval: 5 minutes
-   Mixed-quality data (numeric values + corrupted entries such as
    `"NO DATA"`)

Each file represents a distinct physiological phase across the
monitoring window.

------------------------------------------------------------------------

## Architecture

    wearable-health-signal-analysis/
    │
    ├── data/
    │   ├── phase0.txt
    │   ├── phase1.txt
    │   ├── phase2.txt
    │   └── phase3.txt
    │
    ├── cleaner.py        # Signal validation + numeric coercion
    ├── metrics.py        # Statistical calculations (mean, max, variance, std)
    ├── main.py           # Processing + visualization pipeline
    ├── writeup.md        # Behavioral inference analysis
    ├── test_*.py         # Test-driven validation suite
    └── images/           # Generated time-series plots

------------------------------------------------------------------------

## Data Cleaning Strategy

Sensor data frequently contains:

-   Transmission dropouts
-   Motion artifacts
-   Device interruptions
-   Corrupted string entries

The `filter_nondigits()` function:

-   Strips newline characters
-   Validates numeric-only entries
-   Casts values to integers
-   Returns a cleaned dataset ready for analysis

No statistical libraries are used --- all metrics are implemented
manually to demonstrate computational understanding.

------------------------------------------------------------------------

## Statistical Metrics Implemented

All descriptive statistics are computed using base Python:

-   Mean (via for-loop accumulation)
-   Maximum (via iterative comparison)
-   Variance
-   Standard deviation (√variance)

Values are rounded to two decimal places.

------------------------------------------------------------------------

## Behavioral Inference Logic

Using statistical profiling and visual inspection:

-   Sleep phases exhibit lower mean and maximum heart rate with lower
    variability.
-   Exercise phases exhibit elevated mean, high maximum, and increased
    variance.
-   Awake activity phases fall between these two extremes.

The analysis identifies likely behavioral states for each phase and
provides justification using numerical evidence.

------------------------------------------------------------------------

## Analytical Techniques Demonstrated

-   Time-series signal cleaning
-   Numeric validation and coercion
-   File I/O automation
-   Statistical computation from scratch
-   Phase-based segmentation
-   Variability analysis
-   Behavioral pattern inference
-   Test-driven development workflow

------------------------------------------------------------------------

## Future Enhancements

-   Rolling window heart-rate variability (HRV) analysis
-   Anomaly detection
-   Sleep scoring model
-   Threshold-based classification
-   Feature engineering for ML classification
-   Integration into Streamlit dashboard

------------------------------------------------------------------------

## Key Skills Demonstrated

-   Python modular design
-   Test-driven development
-   Time-series analytics
-   Statistical reasoning
-   Health-tech data interpretation
-   Signal preprocessing

---

## Contact

### Fari Lindo • DataInsideData™

- [GitHub](https://github.com/dataeden)
- [Portfolio](https://datainsidedata.com)
- [LinkedIn](https://www.linkedin.com/in/fari-lindo/)  
- [Email](mailto:contact@datainsidedata.com)

*Tech Hands, a Science Mind, and a Heart for Community™*
