# Weather Classification Data Report

## Dataset Overview

The dataset used for this analysis is named **`weather_classification_data`**. It includes a label called **`Weather Type`** and consists of 10 features. The goal is to classify the weather type based on these features.

## Preprocessing Steps

1. **Null Value Handling**: 
   - The dataset was analyzed and confirmed to have no null values.

2. **Categorical Variables**:
   - Categorical variables were identified and converted to numerical variables using one-hot encoding.

3. **Normalization and Standardization**:
   - Applied normalization and standardization to ensure all features are on a comparable scale.

4. **Visualization**:
   - Various visualization techniques were employed to generate insightful plots for data analysis.

5. **Data Splitting**:
   - The dataset was split into training and testing sets for model evaluation.

## Model Evaluation

Three different models were applied to the dataset:

### 1. Logistic Regression

- **Accuracy**: 0.87
- **Classification Report**:
  - **Precision, Recall, F1-Score, and Support** for each class are detailed.
- **Confusion Matrix**:
  - The confusion matrix shows the counts of true positives, false positives, true negatives, and false negatives.

### 2. Decision Tree

- **Accuracy**: 0.90
- **Classification Report**:
  - **Precision, Recall, F1-Score, and Support** for each class are detailed.
- **Confusion Matrix**:
  - The confusion matrix shows the counts of true positives, false positives, true negatives, and false negatives.

### 3. Random Forest

- **Accuracy**: 0.92
- **Classification Report**:
  - **Precision, Recall, F1-Score, and Support** for each class are detailed.
- **Confusion Matrix**:
  - The confusion matrix shows the counts of true positives, false positives, true negatives, and false negatives.

## Models comparison:
which model is the right one to choose depends on the specicif task that what are the requirements of the task if we talk in terms of accuracy the Random Forest Classifier model gives the highest accuracy among all which leads to a good perfomace of this model as comparitive to others.

## Conclusion

The evaluation of the models provides insights into their performance on the weather classification dataset. The choice of model and the preprocessing steps play a crucial role in achieving optimal classification results.
