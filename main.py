import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis

# Load the data from the specified file path
#add your file path where you saved the CSV file
file_path = r'E:\Healthcare-Diabetes.csv'
data = pd.read_csv(file_path)

# Data Cleaning (you can customize this based on your dataset)
# For example, you can remove missing values or handle outliers here.

# Calculate Mean
mean = data.mean()

# Calculate Median
median = data.median()

# Calculate Standard Deviation
std_dev = data.std()

# Calculate Skewness
data_skewness = skew(data, axis=0)

# Calculate Kurtosis
data_kurtosis = kurtosis(data, axis=0)

# Create a DataFrame to store the results
summary_stats = pd.DataFrame({
    'Mean': mean,
    'Median': median,
    'Standard Deviation': std_dev,
    'Skewness': data_skewness,
    'Kurtosis': data_kurtosis
})

# Display the summary statistics
print(summary_stats)
