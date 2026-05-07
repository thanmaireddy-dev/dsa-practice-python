import pandas as pd

data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6],
    'Exam_Score': [35, 40, 50, 60, 65, 75]
}
df = pd.DataFrame(data)

# Step 2: Display the dataset
print("Dataset:")
print(df)

# Step 3: Dataset information
print("\nDataset Information:")
print(df.info())

# Step 4: Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Step 5: Check for missing values
print("\nMissing Values:")

print(df.isnull())

# Step 6: Separate feature and target
X = df[['Hours_Studied']]
y = df['Exam_Score']
print("\nFeature (X):")
print(X)
print("\nTarget (y):")
print(y)

