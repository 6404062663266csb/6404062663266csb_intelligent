# generate_dataset_model2.py
import pandas as pd
import numpy as np

np.random.seed(42)

hours_sleep = np.random.randint(4, 10, 30)
hours_study = np.random.randint(1, 8, 30)
stress_level = np.random.randint(1, 10, 30)

result = ["Pass" if (s + st > str_level) else "Fail"
          for s, st, str_level in zip(hours_sleep, hours_study, stress_level)]

df = pd.DataFrame({
    "hours_sleep": hours_sleep,
    "hours_study": hours_study,
    "stress_level": stress_level,
    "result": result
})

mask = np.random.rand(*df.shape) < 0.1
df = df.mask(mask)

df.to_csv("student_performance_model2.csv", index=False)
print("CSV Dataset saved as student_performance_model2.csv")