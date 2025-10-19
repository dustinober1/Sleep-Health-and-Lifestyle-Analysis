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
plt.figure(figsize=(12, 8))

# Create subplots for the data description
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Distribution of categorical variables
categorical_cols = ['Gender', 'BMI Category', 'Sleep Disorder']
for i, col in enumerate(categorical_cols):
    if i < 2:  # Only plot first two on top row
        ax = axes[0, i]
        df[col].value_counts().plot(kind='bar', ax=ax)
        ax.set_title(f'Distribution of {col}')
        ax.tick_params(axis='x', rotation=45)

# Plot 2: Distribution of numerical variables
numeric_cols = ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Heart Rate']
ax = axes[1, 0]
df[numeric_cols].hist(bins=15, ax=ax)
ax.set_title('Distribution of Numerical Variables')

# Plot 3: Summary statistics as a heatmap of correlations
correlation_cols = ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Heart Rate', 'Daily Steps']
corr_data = df[correlation_cols].corr()
sns.heatmap(corr_data, annot=True, cmap='coolwarm', center=0, ax=axes[1, 1])
axes[1, 1].set_title('Correlation Matrix of Key Variables')

plt.tight_layout()
plt.savefig('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures/data_description.png', dpi=300, bbox_inches='tight')
plt.show()

# 2. Typical Amount (Minutes) of Physical Activity
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Physical Activity Level', bins=20, kde=True)
plt.title('Distribution of Physical Activity Level (Minutes/Day)')
plt.xlabel('Physical Activity Level (Minutes)')
plt.ylabel('Frequency')
plt.savefig('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures/physical_activity_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# Also create a boxplot to show the distribution details
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['Physical Activity Level'])
plt.title('Box Plot of Physical Activity Level (Minutes/Day)')
plt.ylabel('Physical Activity Level (Minutes)')
plt.savefig('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures/physical_activity_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()

# 3. Analysis of Daily Steps Taken
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Daily Steps', bins=20, kde=True)
plt.title('Distribution of Daily Steps')
plt.xlabel('Daily Steps')
plt.ylabel('Frequency')
plt.savefig('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures/daily_steps_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# Also create a boxplot for daily steps
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['Daily Steps'])
plt.title('Box Plot of Daily Steps')
plt.ylabel('Daily Steps')
plt.savefig('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures/daily_steps_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. Distribution of Heart Rates
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Heart Rate', bins=20, kde=True)
plt.title('Distribution of Heart Rates (bpm)')
plt.xlabel('Heart Rate (bpm)')
plt.ylabel('Frequency')
plt.savefig('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures/heart_rate_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# Boxplot of heart rate to identify potential outliers
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['Heart Rate'])
plt.title('Box Plot of Heart Rates (bpm) - Outliers Visible')
plt.ylabel('Heart Rate (bpm)')
plt.savefig('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures/heart_rate_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()

# Also create a violin plot for heart rate by sleep disorder type
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='Sleep Disorder', y='Heart Rate')
plt.title('Distribution of Heart Rates by Sleep Disorder Type')
plt.xlabel('Sleep Disorder Type')
plt.ylabel('Heart Rate (bpm)')
plt.savefig('/home/dobercode/Sleep-Health-and-Lifestyle-Analysis/outputs/figures/heart_rate_by_disorder.png', dpi=300, bbox_inches='tight')
plt.show()

print("All visualizations have been created and saved to the outputs/figures directory.")