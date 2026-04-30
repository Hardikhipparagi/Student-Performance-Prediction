import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/students.csv")

sns.heatmap(df.corr(), annot=True)
plt.title("Feature Correlation Heatmap")
plt.show()