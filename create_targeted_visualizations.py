import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/sleep_health_and_lifestyle_dataset-sleep_health_and_lifestyle_dataset.csv')

# Set up the plotting style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100

# Create directory for saving figures if it doesn't exist
import os
if not os.path.exists('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures'):
    os.makedirs('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures')

# 1. Data Description Visualization
plt.figure(figsize=(14, 10))

# Create subplots for the data description
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Top left: Distribution of categorical variables (Gender)
df['Gender'].value_counts().plot(kind='bar', ax=axes[0, 0], color=['skyblue', 'lightcoral'])
axes[0, 0].set_title('Distribution of Gender')
axes[0, 0].tick_params(axis='x', rotation=0)

# Top right: Distribution of categorical variables (BMI Category)
df['BMI Category'].value_counts().plot(kind='bar', ax=axes[0, 1], color='lightgreen')
axes[0, 1].set_title('Distribution of BMI Categories')
axes[0, 1].tick_params(axis='x', rotation=45)

# Bottom left: Distribution of categorical variables (Sleep Disorder)
df['Sleep Disorder'].value_counts().plot(kind='bar', ax=axes[1, 0], color='gold')
axes[1, 0].set_title('Distribution of Sleep Disorders')
axes[1, 0].tick_params(axis='x', rotation=0)

# Bottom right: Data Type Summary
# Identify the different data types in the dataset
data_types = df.dtypes.value_counts()
data_types.plot(kind='pie', ax=axes[1, 1], autopct='%1.1f%%')
axes[1, 1].set_title('Distribution of Data Types in Dataset')

plt.tight_layout()
plt.savefig('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures/data_description.png', dpi=300, bbox_inches='tight')
plt.close()  # Close the figure to free memory

# 2. Typical Amount (Minutes) of Physical Activity
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Histogram
sns.histplot(data=df, x='Physical Activity Level', bins=20, kde=True, ax=axes[0])
axes[0].set_title('Distribution of Physical Activity Level (Minutes/Day)')
axes[0].set_xlabel('Physical Activity Level (Minutes)')
axes[0].set_ylabel('Frequency')

# Boxplot
sns.boxplot(y=df['Physical Activity Level'], ax=axes[1])
axes[1].set_title('Box Plot of Physical Activity Level (Minutes/Day)')
axes[1].set_ylabel('Physical Activity Level (Minutes)')

plt.tight_layout()
plt.savefig('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures/physical_activity_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Analysis of Daily Steps Taken
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Histogram
sns.histplot(data=df, x='Daily Steps', bins=20, kde=True, ax=axes[0])
axes[0].set_title('Distribution of Daily Steps')
axes[0].set_xlabel('Daily Steps')
axes[0].set_ylabel('Frequency')

# Boxplot
sns.boxplot(y=df['Daily Steps'], ax=axes[1])
axes[1].set_title('Box Plot of Daily Steps')
axes[1].set_ylabel('Daily Steps')

plt.tight_layout()
plt.savefig('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures/daily_steps_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Distribution of Heart Rates
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Histogram
sns.histplot(data=df, x='Heart Rate', bins=20, kde=True, ax=axes[0])
axes[0].set_title('Distribution of Heart Rates (bpm)')
axes[0].set_xlabel('Heart Rate (bpm)')
axes[0].set_ylabel('Frequency')

# Boxplot to identify outliers
sns.boxplot(y=df['Heart Rate'], ax=axes[1])
axes[1].set_title('Box Plot of Heart Rates (bpm) - Outliers Visible')
axes[1].set_ylabel('Heart Rate (bpm)')

# Violin plot by sleep disorder type
sns.violinplot(data=df, x='Sleep Disorder', y='Heart Rate', ax=axes[2])
axes[2].set_title('Distribution of Heart Rates by Sleep Disorder Type')
axes[2].set_xlabel('Sleep Disorder Type')
axes[2].set_ylabel('Heart Rate (bpm)')

plt.tight_layout()
plt.savefig('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures/heart_rate_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Summary statistics for report
print("Created visualizations for PowerPoint presentation:")
print("1. Data Description - data_description.png")
print("2. Physical Activity Analysis - physical_activity_analysis.png")
print("3. Daily Steps Analysis - daily_steps_analysis.png")
print("4. Heart Rate Distribution - heart_rate_distribution.png")

# Print basic statistics for the presentation
print("\nBasic Statistics Summary:")
print(f"Data Shape: {df.shape}")
print(f"Average Physical Activity Level: {df['Physical Activity Level'].mean():.2f} minutes/day")
print(f"Average Daily Steps: {df['Daily Steps'].mean():.2f} steps")
print(f"Average Heart Rate: {df['Heart Rate'].mean():.2f} bpm")
print(f"Heart Rate Range: {df['Heart Rate'].min():.2f} - {df['Heart Rate'].max():.2f} bpm")
print(f"Heart Rate Std Dev: {df['Heart Rate'].std():.2f} bpm")

# Identify potential heart rate outliers using IQR method
Q1 = df['Heart Rate'].quantile(0.25)
Q3 = df['Heart Rate'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['Heart Rate'] < lower_bound) | (df['Heart Rate'] > upper_bound)]
print(f"Heart Rate Outliers (n): {len(outliers)}")
print(f"Heart Rate Outlier Bounds: {lower_bound:.2f} - {upper_bound:.2f} bpm")