# src/evaluate.py
import pandas as pd
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv("data/students.csv")

X = df[["study_hours", "attendance", "assignments", "midterm"]]
y = df["pass"]

model = joblib.load("models/model.pkl")

pred = model.predict(X)

print("Accuracy:", accuracy_score(y, pred))

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.corr(), annot=True)
plt.title("Feature Correlation Heatmap")
plt.show()