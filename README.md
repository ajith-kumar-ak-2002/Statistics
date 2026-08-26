# Introduction to Statistics

Welcome to the Statistics learning repository! This guide covers the absolute fundamentals of statistics.

---

## 1. What is Statistics?
Statistics is the science of collecting, organizing, presenting, analyzing, and interpreting data to make decisions or draw conclusions about a population.

It is generally divided into two main branches:
*   **Descriptive Statistics:** Organizing, summarizing, and presenting data in an informative way (e.g., calculating the average, drawing charts).
*   **Inferential Statistics:** Drawing conclusions or making predictions about a larger population based on a sample of data.

---

## 2. Population vs. Sample

Understanding the difference between a population and a sample is fundamental to statistical analysis:

| Aspect | Population | Sample |
| :--- | :--- | :--- |
| **Definition** | The complete set of all items or individuals of interest. | A subset of the population selected for study. |
| **Characteristics** | Called **Parameters** (e.g., Population mean: $\mu$). | Called **Statistics** (e.g., Sample mean: $\bar{x}$). |
| **Size** | Represented by $N$ (usually large or infinite). | Represented by $n$ (smaller, manageable size). |
| **Example** | All citizens of a country. | 1,000 citizens surveyed for an election poll. |

---

## 3. Why Do We Use Samples?

In an ideal world, we would analyze the entire population. However, we use samples for several practical reasons:

1.  **Feasibility & Accessibility:** Sometimes it is physically impossible to access the entire population (e.g., counting all the fish in the ocean).
2.  **Cost-Effectiveness:** Collecting data from an entire population (a census) is extremely expensive.
3.  **Time Efficiency:** Surveying or testing a sample takes significantly less time than doing so for the whole population.
4.  **Destructive Testing:** Some tests destroy the product (e.g., testing the crash safety of a car, or the lifespan of lightbulbs). If we tested the entire population, there would be none left to sell!
5.  **Accuracy:** Managing a smaller dataset often leads to fewer data collection errors and higher data quality.

---

## 4. Types of Data

Data can be classified into different types, which determines the kind of statistical methods and visualizations we can apply.

```
                    DATA
                     │
            ┌────────┴────────┐
            ↓                 ↓
      CATEGORICAL          NUMERICAL
         │                    │
      Categories        ┌─────┴─────┐
                        ↓           ↓
                     DISCRETE   CONTINUOUS
                        │           │
                      Count      Measure
```

### A. Categorical Data (Qualitative)
Categorical data represents characteristics or qualities that cannot be measured with numbers but can be sorted into distinct groups or categories.

*   **Definition:** Describes qualities or categories.
*   **Examples:**
    *   Eye color (Blue, Brown, Green)
    *   Blood type (A, B, AB, O)
    *   Customer satisfaction (Satisfied, Neutral, Dissatisfied)
    *   Car brands (Toyota, Ford, Tesla)

### B. Numerical Data (Quantitative)
Numerical data represents values that can be measured or counted and are expressed as numbers.

#### 1. Discrete Data (Count)
*   **Definition:** Numerical values that can be counted individually and have finite or countable values. Typically represented by whole numbers (integers) with no values in between.
*   **Key Concept:** Counted.
*   **Examples:**
    *   Number of children in a household (e.g., 0, 1, 2, 3...)
    *   Number of cars in a parking lot (e.g., 15, 30...)
    *   Number of pages in a book (e.g., 250...)

#### 2. Continuous Data (Measure)
*   **Definition:** Numerical values that can take any value within a range or interval. These values can be infinitely divided into smaller fractions or decimals.
*   **Key Concept:** Measured.
*   **Examples:**
    *   Height of a person (e.g., 172.5 cm, 5'8")
    *   Temperature of a room (e.g., 22.4°C)
    *   Time taken to run a marathon (e.g., 2 hours, 14 minutes, 32 seconds)
    *   Weight of an apple (e.g., 150.25 grams)

---

## 5. What is Mean?
The **Mean** (often referred to as the arithmetic average) is a measure of central tendency. It is calculated by summing up all the values in a dataset and dividing that sum by the total number of values.

### Formula:
*   **Population Mean ($\mu$):** $\mu = \frac{\sum X_i}{N}$
*   **Sample Mean ($\bar{x}$):** $\bar{x} = \frac{\sum x_i}{n}$

Where:
*   $\sum$ denotes the sum of all values.
*   $X_i / x_i$ represents each individual data point.
*   $N / n$ is the total count of data points.

### Example:
For a dataset of test scores: $[85, 90, 75, 95, 80]$
*   Sum = $85 + 90 + 75 + 95 + 80 = 425$
*   Count = $5$
*   Mean = $425 / 5 = 85$

---

## 6. Mean using Python
We can calculate the mean in Python using standard libraries or third-party libraries like `numpy` or `pandas`.

```python
# 1. Using Python's built-in statistics module
import statistics

data = [85, 90, 75, 95, 80]
mean_val = statistics.mean(data)
print(f"Mean (built-in): {mean_val}")

# 2. Using NumPy
import numpy as np

mean_np = np.mean(data)
print(f"Mean (NumPy): {mean_np}")
```

---

## 7. Why Mean is Important in AI/ML
The mean is a foundational building block for many machine learning algorithms and preprocessing techniques:

1.  **Data Imputation (Handling Missing Values):** One common way to fill in missing numerical values in a dataset is to replace them with the mean of that feature/column.
2.  **Feature Scaling (Normalization & Standardization):** 
    *   In **Standardization (Z-score normalization)**, we center data around a mean of 0: $Z = \frac{x - \mu}{\sigma}$.
3.  **Evaluation Metrics:** Metrics like **Mean Squared Error (MSE)** and **Mean Absolute Error (MAE)** rely on averages to calculate error rates.
4.  **Centroid-based Clustering:** In algorithms like **K-Means**, cluster centers (centroids) are calculated as the mean position of all data points in that cluster.
5.  **Baseline Models:** A baseline model for regression tasks might simply predict the mean of the target variable for every input.

---

## 8. Important: Mean can be affected by Outliers
While the mean is useful, it is highly sensitive to **outliers** (extreme values that are much larger or smaller than the rest of the dataset).

### Example:
Consider salaries of 5 employees: \$40k, \$45k, \$50k, \$55k, \$60k.
*   **Mean Salary:** $(40 + 45 + 50 + 55 + 60) / 5 = \$50\text{k}$ (A good representation of the group).

Now, suppose we add a CEO's salary of \$1,000k (outlier):
*   **Dataset:** \$40k, \$45k, \$50k, \$55k, \$60k, \$1,000k.
*   **New Mean Salary:** $(40 + 45 + 50 + 55 + 60 + 1000) / 6 \approx \$208.3\text{k}$

> [!WARNING]
> The mean has jumped to \$208.3k, which does not accurately represent what the typical employee or CEO earns. In datasets with significant outliers or skewed distributions, the **Median** is often a better measure of central tendency.

---

## 9. What is Median?
The **Median** is the middle value in a sorted, ordered list of numbers. Unlike the mean, which is an average of all values, the median is a position-based measure that divides the dataset into two equal halves (50% of the values are below the median, and 50% are above it).

> [!IMPORTANT]
> To find the median, you **must first sort the dataset** in ascending (or descending) order.

### A. Odd Number of Values
If the dataset has an odd number of data points ($n$), the median is the exact middle value.
*   **Formula:** $\text{Median} = \text{Value at position } \left(\frac{n + 1}{2}\right)$
*   **Example:** For sorted dataset $[12, 15, 22, 30, 45]$ (where $n=5$):
    *   $\text{Position} = \frac{5 + 1}{2} = 3^{\text{rd}}\text{ position}$
    *   $\text{Median} = 22$

### B. Even Number of Values
If the dataset has an even number of data points ($n$), there is no single middle value. The median is the average (mean) of the two middle values.
*   **Formula:** $\text{Median} = \frac{\text{Value at position } \left(\frac{n}{2}\right) + \text{Value at position } \left(\frac{n}{2} + 1\right)}{2}$
*   **Example:** For sorted dataset $[10, 15, 20, 25, 30, 35]$ (where $n=6$):
    *   Middle positions are $3^{\text{rd}}$ and $4^{\text{th}}$ (values $20$ and $25$).
    *   $\text{Median} = \frac{20 + 25}{2} = 22.5$

---

## 10. Very Important: Median and Mean are Different
While both the Mean and the Median are measures of central tendency, they differ significantly in how they respond to data distribution:

1.  **Sensitivity to Outliers:**
    *   **Mean:** Extremely sensitive to outliers.
    *   **Median:** Robust/resistant to outliers because it only depends on the position, not the values of all elements.
2.  **Use Cases:**
    *   Use **Mean** for symmetric distributions without extreme outliers (e.g., height, test scores).
    *   Use **Median** for highly skewed distributions or datasets containing extreme outliers (e.g., household income, real estate prices).

---

## 11. Median with Python Using NumPy
We can easily calculate the median using Python's standard `statistics` module or NumPy.

```python
import numpy as np
import statistics

data = [30, 10, 15, 20, 35, 25]  # Unsorted data

# Using NumPy (automatically handles sorting internally)
median_np = np.median(data)
print(f"Median (NumPy): {median_np}")

# Using Python's built-in statistics module
median_builtin = statistics.median(data)
print(f"Median (Built-in): {median_builtin}")
```

---

## 12. What is Mode?
The **Mode** is the value that appears most frequently in a dataset. Unlike the mean and median, the mode can be calculated for both numerical (quantitative) and categorical (qualitative) data.

*   **Example:** In the dataset $[3, 7, 5, 13, 20, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29]$:
    *   The value `23` appears 4 times, which is more than any other value.
    *   **Mode** = $23$

---

## 13. Types of Mode Distributions & No Mode

Depending on the frequencies of the values, a dataset can have one mode, multiple modes, or no mode at all:

### A. Number of Modes:
*   **Unimodal (One mode):** The dataset has exactly one value with the highest frequency.
    *   *Example:* $[4, 5, 5, 6, 7] \rightarrow \text{Mode} = 5$
*   **Bimodal (Two modes):** The dataset has two values that share the highest frequency.
    *   *Example:* $[1, 2, 2, 3, 4, 4, 5] \rightarrow \text{Modes} = 2 \text{ and } 4$
*   **Multimodal (More than two modes):** The dataset has three or more values that share the highest frequency.
    *   *Example:* $[10, 10, 11, 12, 12, 13, 14, 14] \rightarrow \text{Modes} = 10, 12, \text{ and } 14$

### B. No Mode:
If all values in a dataset appear with the same frequency, the dataset is considered to have **no mode**.
*   *Example:* $[1, 2, 3, 4, 5]$ (every number appears exactly once) $\rightarrow \text{No Mode}$

---

## 14. Mode with Python using Pandas
While you can calculate the mode using Python's built-in `statistics` module, **Pandas** is the most common tool used in data science because it easily handles datasets with multiple modes or missing values.

```python
import pandas as pd

# Creating a dataset (with two modes: 5 and 8)
data = [5, 5, 2, 8, 8, 3, 1]

df = pd.Series(data)

# Calculate mode (returns a Series because there can be multiple modes)
modes = df.mode()

print("Modes found:")
print(modes.to_list())  # Output: [5, 8]
```

---

## 15. Mean vs. Median vs. Mode (Summary)

Choosing the right measure of central tendency depends on the data type and distribution shape:

| Feature/Measure | Mean | Median | Mode |
| :--- | :--- | :--- | :--- |
| **Best For** | Symmetric, numerical data without outliers (e.g., test scores, heights). | Skewed, numerical data or datasets with outliers (e.g., salaries). | Categorical data or finding the most common class/value. |
| **Outlier Sensitivity** | **High** (Very sensitive) | **None** (Highly robust) | **None** (Highly robust) |
| **Number of values** | Always unique (1) | Always unique (1) | Can have multiple (None, 1, or more) |
| **Categorical Data?** | No | No | **Yes** |

---

## 16. AI/ML Connection for Mode
Just like mean and median, the mode plays a crucial role in machine learning:

1.  **Categorical Data Imputation:** When preprocessing a dataset with missing values in categorical columns (e.g., "City", "Gender", "Product Type"), we impute (fill in) the missing entries using the **Mode** of that column.
2.  **Classification Algorithms:** Many classification models work by voting. For example, in **K-Nearest Neighbors (KNN)** classification, the algorithm finds the $k$ nearest neighbors to a query point and assigns the class label by taking the **Mode** of those neighbors' classes.
3.  **Ensemble Methods (Majority Voting):** In ensemble learning (like combining multiple distinct models), the final prediction is often decided by taking the **Mode** (majority vote) of all individual model predictions.

---

## 17. What is Range?
The **Range** is the simplest measure of dispersion (spread) in statistics. It is the difference between the maximum (highest) and minimum (lowest) values in a dataset.

### Formula:
$$\text{Range} = X_{\text{max}} - X_{\text{min}}$$

### Example:
For the dataset of daily temperatures (in °C): $[15, 22, 18, 30, 25]$
*   $X_{\text{max}} = 30$
*   $X_{\text{min}} = 15$
*   $\text{Range} = 30 - 15 = 15\text{°C}$

---

## 18. Why is Range Useful?
*   **Simplicity:** It is extremely easy and quick to calculate.
*   **Quick Overview:** It gives an immediate, rough idea of the spread or variability of the data. For example, comparing the temperature range of two cities helps quickly show which one has more volatile weather.
*   **Quality Control:** In manufacturing, range is used in control charts (like R-charts) to monitor whether process variability is staying within acceptable bounds.

---

## 19. Limitations of Range
While easy to compute, the Range has two major drawbacks:
1.  **High Sensitivity to Outliers:** Since it only depends on the two extreme values (min and max), a single outlier will distort the range, rendering it unrepresentative of the rest of the dataset.
    *   *Example:* If a dataset $[4, 5, 6, 5, 4]$ (Range = 2) gets an outlier $100$, the new dataset $[4, 5, 6, 5, 4, 100]$ has a Range of $96$.
2.  **Ignores the Distribution:** The range doesn't tell us anything about how the data points are distributed between the minimum and maximum values. Two datasets could have the same range but completely different spreads in the middle.

---

## 20. Range with Python Using NumPy
We can compute the range in Python using NumPy's `np.ptp()` function (which stands for "peak-to-peak") or by manually subtracting the minimum from the maximum.

```python
import numpy as np

data = [15, 22, 18, 30, 25]

# Method 1: Using NumPy's peak-to-peak (ptp) function
range_np = np.ptp(data)
print(f"Range (using np.ptp): {range_np}")

# Method 2: Manually calculating using np.max and np.min
range_manual = np.max(data) - np.min(data)
print(f"Range (manual): {range_manual}")
```

---

## 21. What is Variance?
**Variance** measures how far a set of numbers is spread out from their average (mean) value. It answers the question: *How much do all the values differ from the mean?*

Unlike the range, which only uses the two extreme values, variance takes every single data point into account.

### The Step-by-Step Process:

```
          Data
           │
           ▼
     Calculate Mean
           │
           ▼
Find difference from Mean
           │
           ▼
 Square the differences
           │
           ▼
        Add them
           │
           ▼
Divide by number of values
           │
           ▼
       Variance
```

---

## 22. Why Square the Differences?
When calculating variance, we subtract the mean from each data point ($x_i - \mu$). If we simply add these differences together without squaring them, the negative and positive values will cancel each other out, resulting in a sum of zero.

By **squaring** the differences:
1.  **Eliminates Negative Signs:** All differences become positive, allowing us to sum them up.
2.  **Penalizes Outliers:** Squaring gives disproportionately more weight to points that lie far from the mean (e.g., a difference of $2$ becomes $4$, but a difference of $10$ becomes $100$).

---

## 23. Population Variance vs. Sample Variance
There is a critical distinction in the denominator when calculating variance for an entire population versus a sample:

| Type | Population Variance ($\sigma^2$) | Sample Variance ($s^2$) |
| :--- | :--- | :--- |
| **Formula** | $\sigma^2 = \frac{\sum (X_i - \mu)^2}{N}$ | $s^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1}$ |
| **Denominator** | Divided by $N$ (Total population size). | Divided by $n - 1$ (Sample size minus 1). |
| **Reasoning** | We have complete data, so we divide by the actual count. | Uses **Bessel's Correction** ($n-1$) to correct bias, making the sample variance a better estimator of the true population variance. |

---

## 24. Variance with Python Using NumPy
NumPy calculates population variance by default (denominator $N$). To compute sample variance, you must set the degrees of freedom parameter `ddof=1` (denominator $n-1$).

```python
import numpy as np

data = [10, 12, 23, 23, 16, 23, 21, 16]

# 1. Population Variance (divides by N)
pop_var = np.var(data)
print(f"Population Variance (N): {pop_var:.4f}")

# 2. Sample Variance (divides by n - 1)
sample_var = np.var(data, ddof=1)
print(f"Sample Variance (n - 1): {sample_var:.4f}")
```

---

## 25. Why Variance Matters in AI/ML
Variance is a cornerstone concept across many areas of Machine Learning and Data Science:

1.  **The Bias-Variance Tradeoff:** A fundamental model performance concept.
    *   **High Variance:** The model is oversensitive to fluctuations in the training data (**overfitting**). It performs well on training data but poorly on unseen test data.
2.  **Feature Selection (Variance Threshold):** Features with very low variance (e.g., a column where almost all values are identical) carry little information, so they are often dropped during preprocessing.
3.  **Dimensionality Reduction (PCA):** Principal Component Analysis (PCA) works by projecting data onto directions of **maximum variance** to retain as much information as possible in fewer dimensions.
4.  **Weight Initialization:** Deep learning models use variance metrics to scale initial weights (e.g., He or Xavier initialization) to prevent vanishing or exploding gradients.

---

## 26. What is a Percentile?

A **Percentile** is a statistical measure that indicates the relative standing of a value within a dataset. Specifically, the $p^{\text{th}}$ percentile is the value below which $p\%$ of the observations in the dataset fall.

*   **Definition:** Position-based measure that divides an ordered dataset into 100 equal parts.
*   **Key Idea:** It tells you how a specific data point compares to the rest of the group.

### Formula for Rank / Position:
To find the position ($k$) of the $p^{\text{th}}$ percentile in a sorted dataset of $n$ elements:

$$k = 1 + \frac{p}{100} \times (n - 1)$$

*(If $k$ is an integer, the percentile is the value at position $k$. If $k$ is not an integer, interpolation between adjacent values is performed.)*

### Real-World Example:
If you take a standardized test and score in the **$85^{\text{th}}$ percentile**:
*   It does **NOT** mean you scored $85\%$ on the test.
*   It means you scored **higher than or equal to $85\%$** of all students who took the test (and only $15\%$ scored higher than you).

> [!NOTE]
> Like the median, data **must be sorted in ascending order** before calculating percentiles.

---

## 27. Percentile vs. Percentage

It is common to confuse **Percentage** and **Percentile**, but they measure fundamentally different concepts:

| Aspect | Percentage (%) | Percentile |
| :--- | :--- | :--- |
| **Definition** | A fraction or ratio expressed as a portion out of 100 ($\frac{\text{Score}}{\text{Total}} \times 100$). | A value indicating the percentage of scores that fall at or below it. |
| **Measurement Type** | Absolute performance measure. | Relative rank / positional measure. |
| **Dependency** | Independent of how others perform. | Fully dependent on the distribution of the entire dataset. |
| **Range** | 0% to 100% (or higher in growth metrics). | 0th to 100th percentile. |
| **Example** | Getting 40 out of 50 on a test is **80%**. | If 40/50 is higher than 90% of class scores, you are in the **90th percentile**. |

---

## 28. Important Percentiles

While any percentile from 0 to 100 can be calculated, certain percentiles are particularly significant in statistics and data analysis:

### A. The Quartiles
Quartiles divide a sorted dataset into four equal parts, each containing 25% of the data:

```
    Min          Q1 (25th)       Q2 (50th)       Q3 (75th)          Max
     │──────────────┼───────────────┼───────────────┼───────────────│
     │   25% Data   │   25% Data    │   25% Data    │   25% Data    │
```

1.  **$25^{\text{th}}$ Percentile ($Q_1$ - First Quartile):** Marks the bottom 25% of data. 25% of values lie below $Q_1$ and 75% lie above.
2.  **$50^{\text{th}}$ Percentile ($Q_2$ - Second Quartile / Median):** Divides the dataset in half. Exactly 50% of values lie below $Q_2$.
3.  **$75^{\text{th}}$ Percentile ($Q_3$ - Third Quartile):** Marks the top 25% (or bottom 75%) of data. 75% of values lie below $Q_3$ and 25% lie above.

> [!TIP]
> The **Interquartile Range (IQR)** measures the spread of the middle 50% of data:
> $$\text{IQR} = Q_3 - Q_1$$

### B. Extreme / Tail Percentiles
*   **$90^{\text{th}}$, $95^{\text{th}}$, and $99^{\text{th}}$ Percentiles:** Used to evaluate extreme values, system latency, SLA compliance, and rare tail events without getting distorted by maximum value single-off anomalies.

---

## 29. Why Percentiles Matter in AI/ML

Percentiles play a critical role in data preprocessing, feature engineering, and model monitoring in Machine Learning:

1.  **Robust Outlier Detection (The IQR Method):**
    Outliers can severely distort ML models. The standard IQR rule identifies potential outliers as any data point ($X$) satisfying:
    $$X < Q_1 - 1.5 \times \text{IQR} \quad \text{or} \quad X > Q_3 + 1.5 \times \text{IQR}$$

2.  **Robust Feature Scaling (`RobustScaler`):**
    Standardization ($\frac{x-\mu}{\sigma}$) and Min-Max scaling are vulnerable to extreme outliers. `RobustScaler` scales features using the median ($Q_2$) and IQR:
    $$X_{\text{scaled}} = \frac{X - Q_2}{Q_3 - Q_1}$$
    This ensures outliers do not compress the majority of inlier data points into a narrow range.

3.  **Model Inference Latency & System Monitoring:**
    Average latency (mean) can mask slow responses. ML Engineers track **P95** ($95^{\text{th}}$ percentile) and **P99** ($99^{\text{th}}$ percentile) latency to guarantee that 99% of users experience fast model prediction times.

4.  **Data Drift Detection:**
    By tracking shifts in $Q_1$, Median, and $Q_3$ of incoming production data over time, ML pipelines can detect distribution changes (data drift) before model accuracy degrades.

5.  **Threshold Tuning in Classification:**
    For imbalanced classification (e.g., fraud detection where only 1% of transactions are fraudulent), model prediction probability thresholds are often chosen using top percentiles (e.g., classifying top 1% probabilities as fraud).

---

## 30. Percentiles with NumPy

NumPy provides two primary functions for computing percentiles and quantiles: `np.percentile()` (accepts 0–100) and `np.quantile()` (accepts 0.0–1.0).

```python

import numpy as np

# Sample dataset: exam scores of 10 students
scores = [45, 55, 60, 65, 70, 78, 82, 88, 92, 98]

# 1. Calculating a single percentile (e.g., 50th percentile = Median)
p50 = np.percentile(scores, 50)
print(f"50th Percentile (Median): {p50}")

# 2. Calculating multiple percentiles at once (Quartiles: Q1, Q2, Q3)
q1, q2, q3 = np.percentile(scores, [25, 50, 75])
print(f"Q1 (25th): {q1}, Q2 (50th): {q2}, Q3 (75th): {q3}")

# Calculating Interquartile Range (IQR)
iqr = q3 - q1
print(f"IQR: {iqr}")

# 3. Using np.quantile (uses fractions from 0.0 to 1.0)
quantiles = np.quantile(scores, [0.25, 0.50, 0.75, 0.95])
print(f"Quantiles (25%, 50%, 75%, 95%): {quantiles}")

# 4. Specifying interpolation methods (NumPy default is 'linear')
p90_nearest = np.percentile(scores, 90, method='nearest')
p90_linear = np.percentile(scores, 90, method='linear')
print(f"90th Percentile (Nearest): {p90_nearest}")
print(f"90th Percentile (Linear): {p90_linear}")
```

---

## 31. What are Quartiles?

**Quartiles** are statistical values that divide a sorted dataset into **four equal parts**, with each part representing $25\%$ of the total data points.

```
                  Sorted Dataset (100% of Data)
 ┌──────────────────┬──────────────────┬──────────────────┬──────────────────┐
 │   First 25%      │   Second 25%     │    Third 25%     │    Fourth 25%    │
 └──────────────────┴──────────────────┴──────────────────┴──────────────────┘
 Min                Q1 (25th)          Q2 (50th)          Q3 (75th)         Max
                                       (Median)
```

### The Three Quartiles:
1.  **$Q_1$ (First Quartile / Lower Quartile):** 
    *   Equal to the **$25^{\text{th}}$ Percentile**.
    *   $25\%$ of data points lie below $Q_1$, and $75\%$ lie above it.
2.  **$Q_2$ (Second Quartile / Median):** 
    *   Equal to the **$50^{\text{th}}$ Percentile**.
    *   Cuts the dataset exactly in half ($50\%$ below, $50\%$ above).
3.  **$Q_3$ (Third Quartile / Upper Quartile):** 
    *   Equal to the **$75^{\text{th}}$ Percentile**.
    *   $75\%$ of data points lie below $Q_3$, and $25\%$ lie above it.

### How to Calculate Quartiles Manually:
1.  **Sort** the dataset in ascending order.
2.  Find **$Q_2$ (Median)** to split the dataset into a lower half and an upper half.
3.  Find the **median of the lower half** to get **$Q_1$**.
4.  Find the **median of the upper half** to get **$Q_3$**.

---

## 32. The Interquartile Range (IQR)

The **Interquartile Range (IQR)** is a measure of statistical dispersion (spread) that represents the range spanned by the middle $50\%$ of an ordered dataset.

### Formula:
$$\text{IQR} = Q_3 - Q_1$$

Where:
*   $Q_3$ = $75^{\text{th}}$ percentile (Upper Quartile)
*   $Q_1$ = $25^{\text{th}}$ percentile (Lower Quartile)

### Why is IQR "The Important Part"?
Unlike the total **Range** ($X_{\text{max}} - X_{\text{min}}$), which relies entirely on the two extreme values and is destroyed by outliers, the **IQR ignores the top 25% and bottom 25% of extreme data points**. 

> [!IMPORTANT]
> The IQR provides a **robust measure of variability** that focuses strictly on the core bulk of the data, making it completely resistant to extreme outliers.

### IQR and the Box Plot (Five-Number Summary)
The IQR forms the foundation of the **Box Plot (Box-and-Whisker Plot)**, which visually summarizes data using 5 key numbers:

```
        Outlier                          Box                         Outlier
           *       |───────────[  Q1  │  Q2  │  Q3  ]───────────|       *
                   ▲           ▲      ▲      ▲      ▲           ▲
              Lower Fence     Min     │    Median  Max     Upper Fence
               (Q1-1.5*IQR)           └─  IQR  ─┘          (Q3+1.5*IQR)
```

---

## 33. Why IQR Matters for AI/ML

In Data Science and Machine Learning, IQR is one of the most widely used metrics for data cleaning and preprocessing:

1.  **Outlier Detection & Removal (1.5 × IQR Rule):**
    Before training a model, extreme values must be identified. Data points outside the "fences" are flagged as outliers:
    *   **Lower Fence:** $Q_1 - 1.5 \times \text{IQR}$
    *   **Upper Fence:** $Q_3 + 1.5 \times \text{IQR}$
    Any data point $X$ where $X < \text{Lower Fence}$ or $X > \text{Upper Fence}$ is an outlier that can be removed, capped (Winsorized), or investigated.

2.  **Robust Feature Scaling (`RobustScaler`):**
    When features contain extreme outliers, standard techniques like `StandardScaler` (Mean & Std) or `MinMaxScaler` fail because the mean and range get pulled by the outliers.
    Scikit-Learn's **`RobustScaler`** uses the Median ($Q_2$) and IQR:
    $$X_{\text{scaled}} = \frac{X - Q_2}{\text{IQR}}$$
    This scales data based on percentiles, keeping inliers concentrated properly without being compressed by extreme values.

3.  **Detecting Skewness & Asymmetry:**
    Comparing $(Q_2 - Q_1)$ against $(Q_3 - Q_2)$ reveals the skewness of a feature:
    *   If $(Q_3 - Q_2) > (Q_2 - Q_1) \rightarrow$ **Right-Skewed** (long right tail).
    *   If $(Q_2 - Q_1) > (Q_3 - Q_2) \rightarrow$ **Left-Skewed** (long left tail).
    *   If $(Q_3 - Q_2) \approx (Q_2 - Q_1) \rightarrow$ **Symmetric**.

4.  **Production Data Monitoring (Covariate Shift):**
    Tracking changes in IQR over time across production model features helps detect data drift. If a feature's IQR suddenly contracts or expands, the model's inputs have changed and retraining may be required.

---

## 34. Quartiles & IQR with Python

We can easily compute Quartiles, IQR, and perform outlier filtering using Python with `numpy` and `scipy.stats`.

```python
import numpy as np
from scipy import stats

# Dataset with 12 values including 2 extreme outliers (5 and 150)
data = [5, 42, 45, 48, 50, 52, 55, 58, 60, 62, 65, 150]

# 1. Compute Quartiles (Q1, Q2/Median, Q3)
q1, q2, q3 = np.percentile(data, [25, 50, 75])
print(f"Q1 (25th percentile): {q1}")
print(f"Q2 (Median):          {q2}")
print(f"Q3 (75th percentile): {q3}")

# 2. Compute Interquartile Range (IQR)
iqr = q3 - q1
# Alternatively using scipy: iqr = stats.iqr(data)
print(f"IQR (Q3 - Q1):        {iqr}")

# 3. Calculate Outlier Fences (1.5 * IQR Rule)
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr
print(f"Lower Fence:          {lower_fence}")
print(f"Upper Fence:          {upper_fence}")

# 4. Identify and filter outliers
outliers = [x for x in data if x < lower_fence or x > upper_fence]
clean_data = [x for x in data if lower_fence <= x <= upper_fence]

print(f"Outliers detected:    {outliers}")      # Output: [5, 150]
print(f"Cleaned dataset:      {clean_data}")    # Core 50% & valid inliers
```

---

## 35. What is an Outlier?

An **Outlier** is a data point that differs significantly from other observations in the same dataset. It is an extreme value that lies far outside the overall distribution pattern of the data.

```
 Normal Data Cluster:  [ 42, 45, 48, 50, 52, 55, 58, 60 ]
 With Extreme Outlier: [ 42, 45, 48, 50, 52, 55, 58, 60 ] . . . . . . . [ 500 ]  <-- Outlier
```

### Common Causes of Outliers:
1.  **Data Entry / Human Error:** Mistyping numbers (e.g., entering $1000$ instead of $10.0$).
2.  **Measurement / Instrument Error:** Faulty sensor readings, network glitches, or equipment miscalibration.
3.  **Sampling Errors:** Inadvertently including data points from a different population (e.g., mixing CEO salaries with entry-level worker salaries).
4.  **Natural Extreme Variability:** Legitimate, real-world extreme values (e.g., net worth of billionaires, rare natural disasters, or high-value fraud transactions).

---

## 36. IQR Method for Detecting Outliers

The **Interquartile Range (IQR) Method** (also known as Tukey's Fences) is the most popular non-parametric technique for identifying outliers because it does not assume a normal distribution.
