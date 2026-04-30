# src/predict.py
import joblib

model = joblib.load("models/model.pkl")

sample = [[5, 80, 70, 65]]

prediction = model.predict(sample)
print("Prediction:", "Pass" if prediction[0] == 1 else "Fail")