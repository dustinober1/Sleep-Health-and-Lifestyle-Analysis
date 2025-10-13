# Presentation Summary for Sleep Health and Lifestyle Analysis

Project objective: Explore relationships between lifestyle factors and sleep duration; build a baseline predictive model for sleep duration.

Dataset: 374 rows × 13 columns. Target: `Sleep Duration`.

Top missingness:

- Sleep Disorder: 219 missing
- Person ID: 0 missing
- Gender: 0 missing
- Age: 0 missing
- Occupation: 0 missing
- Sleep Duration: 0 missing
- Quality of Sleep: 0 missing
- Physical Activity Level: 0 missing
- Stress Level: 0 missing
- BMI Category: 0 missing

Preprocessing steps applied:

- Numeric imputation (median) + scaling
- Categorical imputation (most frequent) + one-hot encoding


Models trained:

- linear_regression: test RMSE=0.162, test R2=0.961, cv RMSE=0.836 (±0.598)
- random_forest: test RMSE=0.072, test R2=0.992, cv RMSE=0.241 (±0.126)

Key figures (files saved under outputs/figures):

- sleep_duration_dist.png — distribution of sleep duration

- correlation_matrix.png — correlation heatmap of numeric features

- sleep_by_gender.png — boxplot of sleep duration by gender

- feature_importances_rf_top20.png — top features from Random Forest

- rf_residuals.png — residual plot for Random Forest
