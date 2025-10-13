Here are detailed study notes for the "Dataset Details" section, which describes the data you'll be using for the project:

## Study Notes: Sleep Health and Lifestyle Dataset

### I. Dataset Overview
* **Topic:** Sleep health and daily habits.
* **Variables Covered:** A wide range of factors, including **demographics** (Gender, Age, Occupation), **sleep metrics** (Duration, Quality of Sleep), **lifestyle** (Physical Activity Level, Stress Level, Daily Steps), **health status** (BMI Category, Blood Pressure, Heart Rate), and the presence of **Sleep Disorders**.
* **Source:** The original dataset is from [Kaggle](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset).

***

### II. Dataset Columns (Features/Variables)

| Column Name | Description | Data Type Notes (for analysis) |
| :--- | :--- | :--- |
| **Person ID** | Identifier for each individual. | (Nominal/ID) – Likely **not used** for descriptive statistics. |
| **Gender** | Male/Female. | (Categorical/Nominal) – Use for counts/proportions. |
| **Age** | Age in years. | (Numeric/Discrete) – Calculate mean, median, range, etc. |
| **Occupation** | Profession of the person. | (Categorical/Nominal) – Use for counts/proportions/grouping. |
| **Sleep Duration (hours)** | Hours of sleep per day. | (Numeric/Continuous) – Calculate mean, SD, visualize distribution. |
| **Quality of Sleep (scale: 1-10)** | Subjective rating (1=low, 10=high). | (Numeric/Ordinal) – Treat as numeric for descriptive stats. |
| **Physical Activity Level (minutes/day)**| Minutes of activity daily. | (Numeric/Continuous) – Analyze central tendency and spread. |
| **Stress Level (scale: 1-10)** | Subjective rating (1=low, 10=high). | (Numeric/Ordinal) – Treat as numeric for descriptive stats. |
| **BMI Category** | BMI category (e.g., Underweight, Normal, Overweight). | (Categorical/Ordinal) – Use for counts/grouping (has an inherent order). |
| **Blood Pressure (systolic/diastolic)** | Systolic over diastolic pressure. | (Numeric/Two values in one column) – Will require **data cleaning/splitting**. |
| **Heart Rate (bpm)** | Resting heart rate in beats per minute. | (Numeric/Discrete) – Calculate mean, median, etc. |
| **Daily Steps** | Number of steps per day. | (Numeric/Discrete) – Analyze distribution and variability. |
| **Sleep Disorder** | Presence or absence of a disorder. | (Categorical/Nominal) – Key target variable; analyze counts and group comparisons. |

***

### III. Details about the Sleep Disorder Column

This column has three distinct categories:

1.  **None:** The individual does not have a specific sleep disorder.
2.  **Insomnia:** Difficulty falling asleep or staying asleep, leading to inadequate or poor-quality sleep.
3.  **Sleep Apnea:** Pauses in breathing during sleep, causing disrupted sleep and potential health risks.

**Key Action for the Project:** When conducting Exploratory Data Analysis (EDA), you should use these categories to compare the descriptive statistics of other variables (e.g., how does the mean **Sleep Duration** differ for individuals with *None*, *Insomnia*, and *Sleep Apnea*?).