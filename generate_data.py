import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

data = pd.DataFrame({
    "study_hours": np.random.randint(1, 10, n),
    "attendance": np.random.randint(50, 100, n),
    "assignments": np.random.randint(40, 100, n),
    "midterm": np.random.randint(30, 100, n)
})

data["final_score"] = (
    data["study_hours"] * 5 +
    data["attendance"] * 0.3 +
    data["assignments"] * 0.3 +
    data["midterm"] * 0.4
)

data["pass"] = (data["final_score"] > 50).astype(int)

data.to_csv("data/students.csv", index=False)
print("Dataset Created!")