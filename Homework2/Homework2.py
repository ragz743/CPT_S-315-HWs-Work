# Import libraries
import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt

# 2a: What is the Data after z-score standardization? (Use the Population Level Equation)
df = pd.read_csv("Automobile_data_tiny.csv")
print("Z-score standardized data: ")
# Find means and standard deviations of each column (pandas library provides .mean() and .std() methods)
means = df.mean()
stds = df.std()
# Create a new Data Frame called df_scores and converted the values in df to z-scores
df_zscores = (df - means) / stds
print(df_zscores)

# 2b: What is the covariance matrix of the standardized Dataset? (Use the Population Level Equation)
# Use Cosine similarity measure (pandas library provides .cov() method)
covar_mat = df_zscores.cov()
print("\nCovariance matrix: ")
print(covar_mat)

# 2c: What are the first principal component and second principal component of this dataset?
# numpy library provides the np.linalg.eig() method, which outputs the eigenvalues and eigenvectors of a matrix
eigenvalues, eigenvectors = np.linalg.eig(covar_mat)
# Captures the first column of eigenvectors as the first Principal Component
print("\nFirst Principle Component: ", eigenvectors[:, 0])
# Captures the second column of eigenvectors as the second Principal Component
print("Second Principle Component: ", eigenvectors[:, 1])

# 3a: Separate the 40 experiments into two groups via a binning method where one group has low water quality (Group 1)
#     and one group has high water quality (Group 2).
# Sort Data Frame by water_pollution in ascending order
df_water1 = pd.read_csv("water_pollution.csv")
df_water1 = df_water1.sort_values(by="water_pollution")
# Make 2 bins for low water quality and high water quality using equal-width method
df_water1["wp_binned"] = pd.cut(df_water1["water_pollution"], bins=2)
print("\n")
print(df_water1)
df_water2 = pd.read_csv("water_pollution.csv")
df_water2 = df_water2.sort_values(by="water_pollution")
# Make 2 bins for low water quality and high water quality using equal-depth method
df_water2["wp_binned"] = pd.qcut(df_water2["water_pollution"], q=2)
print("\n")
print(df_water2)

# 3b: Normalize the Substance A and Substance B amounts based on the min-max normalization (new range [0,1]) for each
#     group and report the normalized values.
df_water2[["substance_a","substance_b"]] = (df_water2[["substance_a","substance_b"]] - df_water2[["substance_a","substance_b"]].min()) / (df_water2[["substance_a","substance_b"]].max() - df_water2[["substance_a","substance_b"]].min())
print("\n")
print(df_water2[["experiment","substance_a","substance_b","wp_binned"]])

# 3c: Draw scatter plots of the normalized substance A and normalized substance B for each group.
df_water2["wp_binned"] = df_water2["wp_binned"].astype(str)                        # Make wp_binned column a string type

group1 = df_water2[df_water2["wp_binned"].isin(["(21.1, 98.3]"])]                  # Group 1: low water quality
x1 = np.array(group1["substance_a"])
y1 = np.array(group1["substance_b"])
plt.scatter(x1, y1, color="red", label="Group 1 (Low Water Quality)")
plt.xlabel("Substance A")
plt.ylabel("Substance B")
plt.title("Group 1: Low Water Quality")
plt.show()

group2 = df_water2[df_water2["wp_binned"].isin(["(5.098999999999999, 21.1]"])]     # Group 2: high water quality
x2 = np.array(group2["substance_a"])
y2 = np.array(group2["substance_b"])
plt.scatter(x2, y2, color="blue", label="Group 2 (High Water Quality)")
plt.xlabel("Substance A")
plt.ylabel("Substance B")
plt.title("Group 2: High Water Quality")
plt.show()

# 3d: Calculate the correlation coefficient (population level) between the normalized substance A and normalized substance B for each group.
# Correlation coefficient of Group 1: low water quality
sumofxy1 = sum((x1 - x1.mean()) * (y1 - y1.mean()))
squaredx1 = sum((x1 - x1.mean()) ** 2)
squaredy1 = sum((y1 - y1.mean()) ** 2)
squarerootxy1 = (squaredx1 * squaredy1) ** 0.5
corr_coe1 = sumofxy1 / squarerootxy1
print("\nCorrelation Coefficient for Group 1: ",corr_coe1)
# Correlation coefficient of Group 2: high water quality
sumofxy2 = sum((x2 - x2.mean()) * (y2 - y2.mean()))
squaredx2 = sum((x2 - x2.mean()) ** 2)
squaredy2 = sum((y2 - y2.mean()) ** 2)
squarerootxy2 = (squaredx2 * squaredy2) ** 0.5
corr_coe2 = sumofxy2 / squarerootxy2
print("Correlation Coefficient for Group 2: ",corr_coe2)

