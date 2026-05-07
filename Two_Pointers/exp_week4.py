import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# Creating a dataset
data = {'Students': [5, 6, 7, 8, 9, 10, 11, 12, 13,14], 'Marks': [53, 66, 78, 89, 90, 92, 94, 96,98,99]}
df = pd.DataFrame(data)
print(df)
# Create a Linear Regression model
x = df[['Students']].values
y = df[['Marks']].values
model = LinearRegression()
model.fit(x, y)
slope = float(model.coef_[0][0])  # Ensure scalar value
intercept = float(model.intercept_[0])  # Ensure scalar value

print(f"slope(m): {slope:.2f}")
print(f"intercept(b): {intercept:.2f}")
print(f"Equation of the Linear Regression: y = {slope:.2f}x + {intercept:.2f}")
# Evaluate model performance
df['Predicted Marks'] = model.predict(x)
# Plot regression line
print(df.head())
plt.scatter(df['Students'], df['Marks'], color='blue', label='Actual Marks')
plt.plot(df['Students'], df['Predicted Marks'], color='red', label='Regression Line')
plt.xlabel('No. of Students')
plt.ylabel('Marks')
plt.title('Simple Linear Regression: Students Vs. Marks')
plt.legend()
plt.show()