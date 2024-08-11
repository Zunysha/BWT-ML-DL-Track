# Used Car Price Prediction Report

## 1. Introduction
This report presents the process of predicting used car prices using machine learning models. The dataset, obtained from PakWheels, includes various features like year, engine size, mileage, and other car characteristics. The main goal is to build a model that accurately predicts car prices based on these features.

## 2. Data Preprocessing

###  Handling Missing Values
- The `assembly` column was dropped due to a high proportion of missing values.
- Missing values in the `body`, `year`, `fuel`, `color`, and `engine` columns were imputed using the most frequent or median values of those columns.
- Rows with missing values in the target variable `price` were removed to ensure the integrity of the predictive model.

###  Encoding Categorical Variables
Categorical features such as `city`, `body`, `make`, `model`, `transmission`, `fuel`, `color`, and `registered` were converted to numerical values using one-hot encoding to make them suitable for the machine learning models.

###  Standardizing Numerical Features
Numerical features including `year`, `engine`, `mileage`, and `price` were standardized to ensure they all had similar scales, which is important for the performance of machine learning algorithms.

###  Converting Boolean Columns
Boolean columns were converted into binary values (1 and 0) to facilitate their use in the machine learning models.

###  Splitting the Data
The dataset was split into training and testing sets, with 80% of the data used for training and 20% for testing. This split allows for model validation and performance evaluation.

## 3. Exploratory Data Analysis

### 3.1 Scatter Plots
A scatter plot was created to visualize the relationship between `mileage` and `price`. The plot helped in understanding the correlation between these two variables.

### 3.2 Box Plots
A box plot was generated to explore the distribution of car prices in the dataset. This helped in identifying outliers and understanding the spread of the data.

## 4. Model Training and Evaluation
Folowing models are trained and evaluated:
- Linear Regression

Linear Regression provided a basic benchmark model with moderate performance.

- Decision Tree Regression

The Decision Tree model outperformed Linear Regression, showing a lower error and better predictive capability.

- Support Vector Regression

Support Vector Regression also performed well, but with higher error compared to the Decision Tree.

## 5. Model Comparison
Among the three models tested, the Decision Tree model demonstrated the best performance in terms of the lowest Mean Squared Error. This suggests that the Decision Tree model is the most suitable for this particular task, given its ability to capture the nonlinear relationships in the data.

## 6. Conclusion
The Decision Tree model was identified as the best-performing model for predicting used car prices in this dataset. However, the choice of model may vary depending on specific task requirements and the need for interpretability, computation time, or other considerations.
