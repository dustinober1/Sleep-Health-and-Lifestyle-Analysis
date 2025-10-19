# Sleep Health and Lifestyle Analysis

## Project Overview

This project analyzes the relationship between sleep health and various lifestyle factors. The analysis examines how demographic factors, physical activity, stress levels, and other lifestyle choices impact sleep quality and patterns. The project aims to provide insights into sleep health trends and identify factors that contribute to better or worse sleep outcomes.

## Dataset

The analysis is based on the Sleep Health and Lifestyle dataset from Kaggle, which contains information about sleep patterns, health indicators, and lifestyle factors for 374 individuals. 

### Variables Included

- **Person ID**: Identifier for each individual
- **Gender**: Male/Female
- **Age**: Age in years
- **Occupation**: Profession of the person
- **Sleep Duration**: Hours of sleep per day
- **Quality of Sleep**: Subjective rating (1=low, 10=high)
- **Physical Activity Level**: Minutes of activity daily
- **Stress Level**: Subjective rating (1=low, 10=high)
- **BMI Category**: BMI category (Underweight, Normal, Overweight, Obese)
- **Blood Pressure**: Systolic over diastolic pressure
- **Heart Rate**: Resting heart rate in beats per minute
- **Daily Steps**: Number of steps per day
- **Sleep Disorder**: Presence or absence of sleep disorders (None, Insomnia, Sleep Apnea)

## Analysis Components

### Data Description
A comprehensive overview of the dataset structure and variable types, including:
- Continuous variables (Sleep Duration, Heart Rate, Daily Steps)
- Integer variables (Age, Physical Activity Level)
- Ordinal variables (Quality of Sleep, Stress Level)
- Nominal/categorical variables (Gender, BMI Category, Sleep Disorder)

### Physical Activity Analysis
Analysis of typical physical activity levels (minutes per day) and their relationship to:
- Sleep quality
- Daily step counts
- Heart rate
- Stress levels

### Daily Steps Analysis
Examination of daily step patterns and their impact on:
- Sleep duration and quality
- Physical fitness indicators
- Overall lifestyle patterns

### Heart Rate Distribution
Analysis of resting heart rates and their correlation with:
- Sleep disorders
- Stress levels
- BMI categories
- Physical activity levels

## Visualizations

The project includes several visualizations to support the analysis:

- Data Description: Shows distributions of key categorical and numerical variables
- Physical Activity: Distribution and box plots of physical activity levels
- Daily Steps: Analysis of step count patterns
- Heart Rate Distribution: Histograms, box plots, and violin plots showing heart rate by sleep disorder type

## Key Findings

- Most participants have moderate physical activity levels (average ~59 minutes/day)
- Daily step counts average around 6,817 steps per day
- Heart rates show normal distribution with some variation by sleep disorder type
- Physical activity positively correlates with sleep quality
- Sleep disorders show distinct patterns in health indicators

## Technical Implementation

The visualizations were created using Python with the following libraries:
- pandas: for data manipulation
- matplotlib/seaborn: for data visualization
- numpy: for numerical operations

## Files in Repository

- `create_targeted_visualizations.py`: Python script to generate visualizations
- `data_description_table.md`: Markdown table with data description
- `physical_activity_slide.txt`: Content for physical activity slide
- `daily_steps_slide.txt`: Content for daily steps slide
- `heart_rate_slide.txt`: Content for heart rate slide
- `outputs/figures/`: Directory containing generated PNG visualizations

## Usage

To recreate the visualizations:
1. Install required libraries: `pip install pandas matplotlib seaborn`
2. Run the visualization script: `python create_targeted_visualizations.py`

The generated visualizations will be saved to the outputs/figures directory for use in your presentation.

## Presentation Template

The visualizations and content created in this project can be directly integrated into a presentation deck analyzing sleep health and lifestyle patterns.

## Project Goals

This project was developed to:
- Describe the sleep health dataset using descriptive statistics
- Identify trends and patterns in sleep quality and related factors
- Understand how lifestyle factors influence sleep health
- Create visualizations for presentation purposes
- Practice exploratory data analysis techniques

## Data Source

Original dataset: [Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset) on Kaggle.