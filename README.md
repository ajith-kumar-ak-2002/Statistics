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
