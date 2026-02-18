# Wearable Health Signal Analysis — Behavioral Inference Writeup

This writeup summarizes findings from four heart-rate time-series files (`phase0–phase3`) sampled every 5 minutes. The objective is to clean noisy wearable telemetry, compute descriptive statistics, and infer likely behavioral states (sleep, exercise, awake activity) from signal characteristics.

---

## Summary of Phase Metrics (Evidence)

Below are the descriptive statistics used to support behavioral inference:

| Phase  | Mean (bpm) | Max (bpm) | Std Dev (bpm) | Interpretation Anchor |
|-------:|-----------:|----------:|--------------:|------------------------|
| Phase0 | 64.59      | 93        | 8.53          | Low mean + low max + stable variability |
| Phase1 | 87.30      | 110       | 9.90          | Moderate mean + moderate max + moderate variability |
| Phase2 | 85.18      | 117       | 13.38         | Elevated max + highest variability + sustained elevation |
| Phase3 | 60.65      | 99        | 11.00         | Lowest mean but more volatility than Phase0 |

> Notes: Mean and max help indicate intensity; standard deviation is used as a volatility proxy (higher variability often indicates movement, transitions, disturbance, or sensor noise).

---

## Question 1

### Why might we have missing values or values that state "NO DATA" in this dataset?

Wearable heart-rate datasets commonly contain missing values or corrupted entries due to real-world collection constraints. Likely causes include:

- Sensor detachment or poor skin contact (temporary loss of signal)
- Motion artifacts and excessive movement disrupting readings
- Connectivity interruptions (Bluetooth/Wi-Fi packet loss)
- Battery/power interruptions or device resets
- Firmware buffering errors that write placeholders (e.g., `"NO DATA"`)

### What is the risk of filtering these values out?

Filtering out invalid readings is necessary for clean calculations, but it can introduce risk if done blindly:

- **Bias risk:** Removing missing intervals can underrepresent periods of elevated heart rate or instability.
- **Loss of diagnostic signal:** Missingness can reflect meaningful events (device removal, distress, sleep disruption).
- **False stability:** Aggressively filtering can artificially lower variance and make the signal look “healthier” than reality.
- **Operational blind spots:** If missingness is frequent, it may indicate data reliability issues relevant to product design.

In a production health-tech pipeline, these values would typically be tracked with data-quality flags (rate of missingness, dropout windows, and anomaly reporting), not simply discarded.

---

## Question 2

### In which phase does sleep occur? Provide numerical evidence.

Sleep is most consistent with **Phase0**, based on the expected sleep signature: lower maximum heart rate and relatively stable variability.

- **Phase0:** mean = **64.59 bpm**, max = **93 bpm**, std dev = **8.53 bpm**
  - Lower max compared to higher-activity phases, and comparatively stable variability suggests sustained low-intensity physiology.

**Phase3** also shows sleep-like characteristics due to its low mean, but appears less stable:

- **Phase3:** mean = **60.65 bpm**, max = **99 bpm**, std dev = **11.00 bpm**
  - While the mean is the lowest across all phases, the **higher standard deviation** suggests more volatility, which could represent lighter sleep, transitions, disturbances, or sensor noise.

**Conclusion:** Primary sleep phase = **Phase0** (most stable). Phase3 may represent a secondary sleep segment or a more disturbed period.

---

## Question 3

### In which phase does exercise occur? Provide numerical evidence.

Exercise is most consistent with **Phase2**, based on the expected exercise signature: higher maximum heart rate, increased variability, and sustained elevated periods.

- **Phase2:** mean = **85.18 bpm**, max = **117 bpm**, std dev = **13.38 bpm**
  - Highest max heart rate across all phases and the **largest variability**, indicating a strong intensity period with dynamic exertion/recovery cycles.

Visual inspection further supports this: the time-series shows a sustained elevation (often ~100–115 bpm range) for an extended interval before tapering down, consistent with a workout segment followed by recovery.

**Conclusion:** Exercise phase = **Phase2**.

---

## Question 4

### In which phase do we notice regular awake activity (moderate mean, moderate variability)?

Regular awake activity (non-exercise) typically sits between sleep and exercise:

- higher mean than sleep,
- lower max than exercise,
- moderate variability from day-to-day movement.

This pattern best matches **Phase1**:

- **Phase1:** mean = **87.30 bpm**, max = **110 bpm**, std dev = **9.90 bpm**
  - Higher baseline than sleep, but lower max and lower volatility than the exercise phase.

**Conclusion:** Awake activity phase = **Phase1**.

---

## Limitations

- Heart rate alone cannot perfectly classify behavioral states (no accelerometer, no respiration, no HRV features).
- Some spikes/variability may be due to sensor artifacts rather than physiology.
- Filtering corrupted entries is necessary, but missingness patterns should ideally be analyzed as a signal-quality metric.

---

## Future Enhancements

- Rolling-window HRV features (RMSSD proxy if R–R intervals available; otherwise variability windows).
- Anomaly detection (spike detection, dropout windows, artifact flags).
- Rule-based classifier → logistic regression / tree model for phase classification.
- Sleep scoring v1 using duration, stability (variance), and spike count.

---

## References (General Ranges)

Common adult resting heart rate often falls between **~60–100 bpm**, and sleep commonly trends lower than daytime activity.
(These ranges vary widely by individual fitness, age, medication, and health conditions.)
