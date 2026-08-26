# pyrefly: ignore [missing-import]
"""
Comprehensive Statistics Examples in Python
Covers all concepts from README.md:
1. Mean (Built-in & NumPy)
2. Median (Built-in & NumPy)
3. Mode (Pandas)
4. Range (NumPy ptp & manual)
5. Variance (Population vs Sample ddof)
6. Percentiles & Quantiles (NumPy)
7. Quartiles & IQR (Outlier Detection)
"""

import statistics
# pyrefly: ignore [missing-import]
import numpy as np
import pandas as pd
# pyrefly: ignore [missing-import]
from scipy import stats

print("==================================================")
print("1. MEAN EXAMPLES (Section 6)")
print("==================================================")
mean_data = [85, 90, 75, 95, 80]
mean_val = statistics.mean(mean_data)
mean_np = np.mean(mean_data)
print(f"Dataset: {mean_data}")
print(f"Mean (built-in): {mean_val}")
print(f"Mean (NumPy):    {mean_np}\n")


print("==================================================")
print("2. MEDIAN EXAMPLES (Section 11)")
print("==================================================")
median_data = [30, 10, 15, 20, 35, 25]  # Unsorted
median_np = np.median(median_data)
median_builtin = statistics.median(median_data)
print(f"Dataset: {median_data}")
print(f"Median (NumPy):    {median_np}")
print(f"Median (Built-in): {median_builtin}\n")


print("==================================================")
print("3. MODE EXAMPLES (Section 14)")
print("==================================================")
mode_data = [5, 5, 2, 8, 8, 3, 1]  # Bimodal: 5 and 8
df = pd.Series(mode_data)
modes = df.mode()
print(f"Dataset: {mode_data}")
print(f"Modes found (Pandas): {modes.to_list()}\n")


print("==================================================")
print("4. RANGE EXAMPLES (Section 20)")
print("==================================================")
range_data = [15, 22, 18, 30, 25]
range_np = np.ptp(range_data)
range_manual = np.max(range_data) - np.min(range_data)
print(f"Dataset: {range_data}")
print(f"Range (using np.ptp): {range_np}")
print(f"Range (manual max-min): {range_manual}\n")


print("==================================================")
print("5. VARIANCE EXAMPLES (Section 24)")
print("==================================================")
var_data = [10, 12, 23, 23, 16, 23, 21, 16]
pop_var = np.var(var_data)          # ddof=0 default (N)
sample_var = np.var(var_data, ddof=1) # ddof=1 (n - 1)
print(f"Dataset: {var_data}")
print(f"Population Variance (N):   {pop_var:.4f}")
print(f"Sample Variance (n - 1):   {sample_var:.4f}\n")


print("==================================================")
print("6. PERCENTILES & QUANTILES EXAMPLES (Section 30)")
print("==================================================")
scores = [45, 55, 60, 65, 70, 78, 82, 88, 92, 98]
p50 = np.percentile(scores, 50)
q1, q2, q3 = np.percentile(scores, [25, 50, 75])
quantiles = np.quantile(scores, [0.25, 0.50, 0.75, 0.95])
p90_nearest = np.percentile(scores, 90, method='nearest')
p90_linear = np.percentile(scores, 90, method='linear')

print(f"Scores Dataset: {scores}")
print(f"50th Percentile (Median): {p50}")
print(f"Quartiles (Q1, Q2, Q3):   {[q1, q2, q3]}")
print(f"Quantiles (25%,50%,75%,95%): {quantiles}")
print(f"90th Percentile (Nearest): {p90_nearest}")
print(f"90th Percentile (Linear):  {p90_linear}\n")


print("==================================================")
print("7. QUARTILES & IQR OUTLIER DETECTION (Section 34)")
print("==================================================")
iqr_data = [5, 42, 45, 48, 50, 52, 55, 58, 60, 62, 65, 150]
q1_iqr, q2_iqr, q3_iqr = np.percentile(iqr_data, [25, 50, 75])
iqr_val = q3_iqr - q1_iqr
scipy_iqr = stats.iqr(iqr_data)

lower_fence = q1_iqr - 1.5 * iqr_val
upper_fence = q3_iqr + 1.5 * iqr_val

outliers = [x for x in iqr_data if x < lower_fence or x > upper_fence]
clean_data = [x for x in iqr_data if lower_fence <= x <= upper_fence]

print(f"Dataset with Outliers: {iqr_data}")
print(f"Q1 (25th):  {q1_iqr}")
print(f"Q2 (50th):  {q2_iqr}")
print(f"Q3 (75th):  {q3_iqr}")
print(f"IQR (Q3-Q1): {iqr_val} (SciPy: {scipy_iqr})")
print(f"Lower Fence: {lower_fence}")
print(f"Upper Fence: {upper_fence}")
print(f"Outliers Detected: {outliers}")
print(f"Cleaned Dataset:   {clean_data}\n")


print("==================================================")
print("8. OUTLIER DETECTION WITH PYTHON (Section 40)")
print("==================================================")
data = np.array([10, 12, 13, 14, 15, 16, 18, 20, 22, 100])

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = data[(data < lower) | (data > upper)]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower:", lower)
print("Upper:", upper)
print("Outliers:", outliers)
print("==================================================")