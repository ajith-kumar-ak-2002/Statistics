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
