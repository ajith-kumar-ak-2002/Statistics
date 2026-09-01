# Statistics for Data Science & Machine Learning

Welcome to the Statistics learning repository! This guide covers the absolute fundamentals of statistics, probability, and hypothesis testing, tailored specifically for Data Analysts, Data Scientists, and Machine Learning Engineers.

---

## 1. Introduction to Statistics

Statistics is the science of collecting, organizing, presenting, analyzing, and interpreting data to make decisions or draw conclusions about a population.

### Branches of Statistics
*   **Descriptive Statistics:** Organizing, summarizing, and presenting data in an informative way (e.g., calculating the average, drawing charts).
*   **Inferential Statistics:** Drawing conclusions or making predictions about a larger population based on a sample of data.

### Population vs. Sample
| Aspect | Population | Sample |
| :--- | :--- | :--- |
| **Definition** | The complete set of all items or individuals of interest. | A subset of the population selected for study. |
| **Characteristics** | Called **Parameters** (e.g., Population mean: $\mu$). | Called **Statistics** (e.g., Sample mean: $\bar{x}$). |
| **Size** | Represented by $N$ (usually large or infinite). | Represented by $n$ (smaller, manageable size). |

**Why Do We Use Samples?**
Real-world datasets are huge. Analyzing an entire population is often impossible, too expensive, or time-consuming. Samples allow us to draw highly accurate conclusions efficiently.

### Types of Data
*   **Categorical Data (Qualitative):** Describes qualities or categories (e.g., Eye color, Car brands, Blood type).
*   **Numerical Data (Quantitative):** Values that can be measured or counted.
    *   **Discrete (Counted):** Whole numbers (e.g., Number of children, cars in a lot).
    *   **Continuous (Measured):** Any value within a range, including decimals (e.g., Height, Temperature, Time).

---

## 2. Descriptive Statistics & Central Tendency

Measures of central tendency help us find the "middle" or "typical" value of a dataset.

### A. Mean (Average)
The sum of all values divided by the total number of values.
*   **Best for:** Symmetric, numerical data without outliers.
*   **Caution:** Extremely sensitive to outliers.

### B. Median
The middle value in a sorted dataset (50% of values are below, 50% are above).
*   **Best for:** Skewed distributions or data with extreme outliers.
*   **Robustness:** Not affected by outliers.
*   **Interview Question:** *Why would you use median instead of mean?*
    **Answer:** When data contains outliers.

### C. Mode
The value that appears most frequently.
*   **Best for:** Categorical data.
*   **Properties:** Can be unimodal, bimodal, multimodal, or have no mode at all.

### Python Example: Central Tendency
```python
import numpy as np
from scipy import stats

data = [10, 15, 15, 20, 25, 30, 100] # Contains an outlier (100)

print(f"Mean:   {np.mean(data):.2f}")   # Pulled up by outlier
print(f"Median: {np.median(data)}")     # Unaffected by outlier
print(f"Mode:   {stats.mode(data)[0]}")
```

---

## 3. Measures of Dispersion (Spread)

Dispersion measures how spread out the data points are from the center.

### A. Range
The difference between the maximum and minimum values ($Max - Min$). 
*   **Limitation:** Highly sensitive to outliers.

### B. Variance
Measures how far a set of numbers is spread out from their mean. We square the differences to eliminate negative signs and penalize outliers.
*   **Population Variance ($\sigma^2$):** Divides by $N$.
*   **Sample Variance ($s^2$):** Divides by $n-1$ (Bessel's Correction) to remove bias.

### C. Standard Deviation
The square root of the variance. It is expressed in the same units as the original data, making it easier to interpret.

### Python Example: Spread
```python
import numpy as np

data = [15, 22, 18, 30, 25]

print(f"Range:              {np.ptp(data)}")
print(f"Sample Variance:    {np.var(data, ddof=1):.2f}")
print(f"Standard Deviation: {np.std(data, ddof=1):.2f}")
```

---

## 4. Percentiles, Quartiles, and Distributions

### Percentiles and Quartiles
A **Percentile** indicates the relative standing of a value (e.g., scoring in the 90th percentile means you scored better than 90% of people).

**Quartiles** divide sorted data into four equal parts:
*   **Q1 (25th Percentile):** Bottom 25% of data.
*   **Q2 (50th Percentile):** The Median.
*   **Q3 (75th Percentile):** Top 25% of data.

**Interquartile Range (IQR):** Measures the spread of the middle 50% of the data ($IQR = Q3 - Q1$). It is highly robust to outliers.

### Data Distributions
*   **Normal Distribution (Bell Curve):** Symmetric distribution where Mean = Median = Mode.
*   **Skewed Distribution:** Asymmetric (Long left or right tail).
*   **Uniform Distribution:** All outcomes are equally likely.

**Z-Score:** Measures how many standard deviations a data point is from the mean in a normal distribution.

---

## 5. Outliers

An **outlier** is an extreme value that lies far outside the overall pattern of the data. 

> [!IMPORTANT]
> Outlier ≠ Error. Some are mistakes (Data Entry), but others are valid extreme events (e.g., fraud, billionaires). Only remove them if they are confirmed errors.

### The 1.5 × IQR Method
The most common way to mathematically flag outliers:
1.  Calculate IQR ($Q3 - Q1$).
2.  **Lower Fence:** $Q1 - (1.5 \times IQR)$
3.  **Upper Fence:** $Q3 + (1.5 \times IQR)$
4.  Any value outside these fences is an outlier.

### Handling Outliers in AI/ML
*   **Trimming:** Removing the rows entirely.
*   **Winsorization (Capping):** Replacing outliers with the fence values.
*   **Log Transformation:** Applying $\log(X)$ to compress long tails.
*   **Robust Preprocessing:** Using `RobustScaler` (Median & IQR) instead of `StandardScaler`.

---

## 6. Probability Basics

Probability is the mathematical foundation of Machine Learning.

### Key Concepts
*   **Probability Rules:** Values range from 0 to 1. Total probability = 1.
*   **Conditional Probability:** The probability of an event occurring given that another event has already occurred.
*   **Independent Events:** The outcome of one event does not affect the other.

### Bayes' Theorem
A formula that describes how to update the probabilities of hypotheses when given evidence.
*   **Examples:** Predicting if a healthcare claim is fraudulent, medical diagnosis probabilities.
*   **Used heavily in:** Naive Bayes algorithm, Spam filtering, Medical predictions.

---

## 7. Hypothesis Testing & A/B Testing

### Hypothesis Testing
Used to determine if there is enough evidence in a sample to draw conclusions about a population.
*   **Null Hypothesis (H₀):** The default assumption (no effect / no difference).
*   **Alternative Hypothesis (H₁):** What you are trying to prove (there is an effect / difference).
*   **P-Value:** The probability of obtaining the observed results if the null hypothesis is true.
*   **Confidence Intervals:** A range of values that likely contain the population parameter.

**Rule of Thumb:**
If p-value < 0.05 $\rightarrow$ Reject the null hypothesis.

*(Very common topic in Data Analyst/Scientist interviews. Example: "Does a new process reduce claim processing time?")*

### A/B Testing
A practical application of hypothesis testing common in tech companies.
*   **Example:** Comparing Version A vs Version B of a webpage.
*   **Compare metrics:** Click-through rates, Conversion rates.
*   **Used heavily in:** Product analytics, Marketing analytics, Data science.

---

## 8. Correlation & Sampling

### Correlation
Measures the strength and direction of a linear relationship between two variables.
*   **Positive Correlation:** As X goes up, Y goes up (e.g., Study hours vs exam scores).
*   **Negative Correlation:** As X goes up, Y goes down (e.g., Patient age vs immune system strength).
*   **No Correlation:** No apparent relationship.
*   **Tools:** Pearson Correlation Coefficient, Correlation Matrix.

> [!WARNING]
> **Correlation does not imply causation.** Just because two things move together does not mean one causes the other.

### Sampling Techniques
*   **Random Sampling:** Every member of the population has an equal chance of selection.
*   **Stratified Sampling:** Dividing the population into subgroups (strata) and taking a random sample from each.

### The Central Limit Theorem (CLT)
**Very Important:** The CLT states that regardless of the original distribution of the data, the distribution of the *sample means* tends to become a normal distribution (bell curve) as the sample size increases. 
*This concept mathematically supports many statistical and ML techniques.*
