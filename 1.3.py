print("Divyadharshini U G 24BAD023\n")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:/Users/divya/Documents/python/1/Housing.csv", encoding="latin1")

print("top 5 rows of dataset\n")
print(df.head())
print("\n")


print("dataset information\n")
print(df.info())
print("\n")

print("check for missing values\n")
print(df.isnull().sum())
print("\n")

print("scatter plotting\n")
plt.scatter(df['area'], df['price'])
plt.title("Area vs Price")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()

print("heatmaps\n")
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()








