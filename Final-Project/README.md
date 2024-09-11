# COVID-19 Detection Project

## About Dataset

### Context
The global outbreak of COVID-19 has emphasized the critical need for accurate and timely diagnosis. To develop an efficient AI-based diagnostic system, we have curated a dataset of chest X-ray images from various sources and research papers. This dataset serves as a comprehensive resource for training CNN models to automate the diagnosis process.

### Content
The dataset comprises posteroanterior (PA) view chest X-ray images, including those of normal, viral, and COVID-19 affected patients, totaling 1709 images. It has been utilized in the COVID Lite paper, demonstrating promising results with a novel CNN-based solution.

## Data Exploration

### Class Distribution
The dataset exhibits a class distribution across the three categories: COVID, Normal, and Viral. Visualization reveals that the COVID class is less represented compared to others.

### Sample Images
Sample images from each class are displayed to provide a visual understanding of the dataset.

### Image Size Distribution
Exploration of image sizes indicates variations across the dataset, necessitating preprocessing steps for model training.

## Data Preprocessing

Data preprocessing involves tasks such as labeling, resizing, and normalization to prepare the dataset for model training.

## CNN Model

### Architecture
A Convolutional Neural Network (CNN) model is designed to classify chest X-ray images into COVID, Normal, and Viral classes. The architecture consists of convolutional layers followed by max-pooling, dropout, and dense layers.

### Training
The model is trained on the preprocessed dataset using image data generators for efficient handling of large datasets.

### Evaluation
Evaluation metrics include loss, accuracy, confusion matrix, and classification report to assess model performance.

## VGG-16 Model

### Transfer Learning
Utilizing transfer learning with the VGG-16 architecture enhances the model's capacity to learn intricate features from the images.

### Training and Evaluation
Similar to the CNN model, the VGG-16 model undergoes training and evaluation processes to determine its effectiveness in COVID-19 detection.

## Flask App Integration

A Flask web application is developed to provide an interactive interface for users to upload chest X-ray images and obtain predictions using the trained models. The Flask app serves as a practical demonstration of real-world deployment and utilization of the COVID-19 detection models.

## Conclusion

The COVID-19 detection project showcases the development and evaluation of CNN and VGG-16 models for automated diagnosis using chest X-ray images. With high accuracy and robust performance, these models contribute to the ongoing efforts in combating the COVID-19 pandemic.

