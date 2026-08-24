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
