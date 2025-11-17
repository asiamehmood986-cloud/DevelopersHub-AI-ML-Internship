# Task 1: Iris Dataset Exploration & Visualization

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset("iris")

# Display basic information
print("Shape of dataset:", iris.shape)
print("\nColumn names:", iris.columns.tolist())
print("\nFirst 5 rows:\n", iris.head())

# Summary info
print("\nDataset Info:")
print(iris.info())

print("\nSummary Statistics:")
print(iris.describe())

# -------- VISUALIZATIONS --------

# Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=iris, x="sepal_length", y="petal_length", hue="species")
plt.title("Sepal Length vs Petal Length")
plt.show()

# Histograms
iris.hist(figsize=(10, 8))
plt.suptitle("Histograms of Iris Features")
plt.show()

# Box Plots
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris)
plt.title("Boxplot of Iris Dataset Features")
plt.show()

