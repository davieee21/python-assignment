# ===========================================
# Iris Dataset Analysis - Data Loading & Exploration
# ===========================================

# Import necessary libraries
import pandas as pd                          # For data manipulation and analysis
from sklearn.datasets import load_iris       # To load the built-in Iris dataset

# Load the Iris dataset
try:
    iris = load_iris()  # Load the dataset from sklearn
    # Convert the data into a pandas DataFrame with appropriate column names
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    
    # Add a new column 'species' by decoding target integers into category labels
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    # Confirmation message
    print("✅ Dataset loaded successfully.")
except Exception as e:
    # If an error occurs during loading, display it
    print("❌ Error loading dataset:", e)

# Display the first 5 rows of the DataFrame to understand the structure
print("\n🔍 First 5 rows of the dataset:")
print(df.head())

# Display information about the dataset including column names, data types, and non-null counts
print("\nℹ️ Dataset Information:")
print(df.info())

# Check for missing values in each column to ensure data quality
print("\n🔎 Missing Values in Each Column:")
print(df.isnull().sum())

# ===========================================
# Step 3: Data Cleaning - Handling Missing Values
# ===========================================

# Check again if any missing values exist (redundant here, but reinforces clean practice)
missing_values = df.isnull().sum().sum()

if missing_values == 0:
    print("\n✅ No missing values found. Dataset is clean.")
else:
    # Option 1: Drop rows with missing values
    # df.dropna(inplace=True)

    # Option 2: Fill missing values with column mean (if applicable)
    # df.fillna(df.mean(), inplace=True)

    # Let the user know what action was taken
    print(f"\n⚠️ Found {missing_values} missing values. Please review cleaning options.")

# ===========================================
# Step 4: Basic Data Analysis
# ===========================================

# 📊 Summary statistics of all numerical columns
print("\n📈 Basic Statistical Summary:")
print(df.describe())  # Shows count, mean, std, min, max, and quartiles

# 🧪 Grouping data by 'species' and computing mean for each feature
print("\n📊 Mean values of each feature grouped by species:")
grouped_means = df.groupby('species').mean(numeric_only=True)
print(grouped_means)

# 🧠 Observation example: You can manually analyze differences between species
print("\n🔍 Observations:")
print("- Setosa has the smallest petal length and width.")
print("- Virginica generally has the largest values across features.")
print("- Sepal width is slightly higher in Setosa than the others.")

# ===========================================
# Step 5: Visualizations - Line Chart for Sepal Length
# ===========================================

# Import necessary libraries
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import seaborn as sns

# Set Seaborn style for better visuals
sns.set(style="whitegrid")

# 📈 Line chart of sepal length for all 150 samples
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal length (cm)'], color='blue', label='Sepal Length')

# Add title and labels
plt.title('Trend of Sepal Length Across Iris Samples', fontsize=16)
plt.xlabel('Sample Index', fontsize=14)
plt.ylabel('Sepal Length (cm)', fontsize=14)

# Display legend and tighten layout
plt.legend()
plt.tight_layout()

# Show the plot (for interactive visualization)
plt.show()

# Optionally, save the plot to a file
plt.savefig("sepal_length_trend.png")

# ===========================================
# Step 6: Visualization - Bar Chart: Avg Petal Length per Species
# ===========================================

# Calculate average petal length per species
avg_petal_length = df.groupby('species')['petal length (cm)'].mean()

# Create a bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x=avg_petal_length.index, y=avg_petal_length.values, palette="viridis")

# Customize plot
plt.title('Average Petal Length by Iris Species', fontsize=16)
plt.xlabel('Species', fontsize=14)
plt.ylabel('Average Petal Length (cm)', fontsize=14)

# Add value labels on top of each bar
for index, value in enumerate(avg_petal_length.values):
    plt.text(index, value + 0.02, f"{value:.2f}", ha='center', fontsize=12)

plt.tight_layout()
plt.show()

# Optionally save to file
plt.savefig("avg_petal_length_bar.png")

# ===========================================
# Step 7: Visualization - Histogram: Petal Length Distribution
# ===========================================

# Create a histogram to show distribution of petal length
plt.figure(figsize=(8, 6))
sns.histplot(df['petal length (cm)'], bins=20, kde=True, color='teal')

# Customize plot
plt.title('Distribution of Petal Length', fontsize=16)
plt.xlabel('Petal Length (cm)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

plt.tight_layout()
plt.show()

# Optionally save the plot
plt.savefig("petal_length_distribution.png")

# ===========================================
# Step 8: Visualization - Scatter Plot
# ===========================================

# Create scatter plot with species-based coloring
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df,
                x='sepal length (cm)',
                y='petal length (cm)',
                hue='species',
                palette='Set1')

# Customize plot
plt.title('Sepal Length vs Petal Length by Species', fontsize=16)
plt.xlabel('Sepal Length (cm)', fontsize=14)
plt.ylabel('Petal Length (cm)', fontsize=14)
plt.legend(title='Species')
plt.tight_layout()
plt.show()

# Optionally save the plot
plt.savefig("sepal_vs_petal_scatter.png")
