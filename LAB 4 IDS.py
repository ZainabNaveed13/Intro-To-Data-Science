import pandas as pd
import numpy as np

# Load the iris dataset
df = pd.read_csv('iris.csv')

# Task 1: Data Inspection and Missing Value Handling
print("Missing values count:")
print(df.isnull().sum())

# Handle missing values in numeric columns
df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']] = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].fillna(df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].mean())

# Handle missing values in categorical column
df['Species'] = df['Species'].fillna(df['Species'].mode()[0])

# Task 2: Data Cleaning and Transformation
# Remove duplicate entries
df = df.drop_duplicates()

# Create a new column for petal area
df['PetalArea'] = df['PetalLengthCm'] * df['PetalWidthCm']

# Drop rows with any remaining missing values
df = df.dropna()

# Task 3: Aggregation and Transformation
# Convert categorical data to numeric
df['Species'] = pd.Categorical(df['Species']).codes

# Aggregation
agg_df = df.groupby('Species')[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].mean()

# Task 4: Advanced Reshaping
# Reshape the data
melt_df = pd.melt(df, id_vars=['Id', 'Species'], value_vars=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'], var_name='Measurement', value_name='Value')
