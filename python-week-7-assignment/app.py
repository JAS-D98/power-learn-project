import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Loading the iris dataset
try:
    iris_data = load_iris()
    df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)
    print("Data loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display first 5 rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# View structure
print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# Droping missing values if any
df.dropna(inplace=True)

# Descriptive statistics
print("\nDescriptive statistics:")
print(df.describe())

# Mean of features grouped by species
grouped = df.groupby("species").mean()
print("\nMean of features grouped by species:")
print(grouped)

# Observations from grouping
print("\nObservations:")
print("- Setosa has shorter petals compared to the other two species.")
print("- Virginica seems to have larger measurements overall.")

# Data Visualizations

# Line plot - using index to simulate a timeline
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["sepal length (cm)"], label='Sepal Length')
plt.plot(df.index, df["petal length (cm)"], label='Petal Length')
plt.title("Sepal and Petal Length over Samples")
plt.xlabel("Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.grid(True)
plt.show()

# Bar chart - average petal length by species
plt.figure(figsize=(8, 6))
sns.barplot(x=grouped.index, y=grouped["petal length (cm)"])
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# Histogram - sepal width distribution
plt.figure(figsize=(8, 6))
plt.hist(df["sepal width (cm)"], bins=15, color='lightblue', edgecolor='black')
plt.title("Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Count")
plt.show()

# Scatter plot - Sepal vs Petal length
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()
