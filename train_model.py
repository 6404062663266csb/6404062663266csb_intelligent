import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv("bmi_data.csv")

df["Gender"] = df["Gender"].map({
    "Male": 0,
    "Female": 1
})

X = df[["Weight", "Height", "Age", "Gender"]]
y = df["Label"]

le = LabelEncoder()
y_encoded = le.fit_transform(y)

model = DecisionTreeClassifier()
model.fit(X, y_encoded)

joblib.dump(model, "bmi_model.pkl")
joblib.dump(le, "label_encoder.pkl")

print("เสร็จ")