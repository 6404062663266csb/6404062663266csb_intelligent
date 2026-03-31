import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# 📌 โหลดข้อมูล
df = pd.read_csv("student_data.csv")

# 📌 แยก feature / target
X = df[["Hours_Studied","Sleep_Hours","Attendance","Previous_Grade","Internet_Usage"]]
y = df["Pass"]

# 📌 encode label (Pass/Fail → 0/1)
le = LabelEncoder()
y = le.fit_transform(y)

# 📌 split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================================================
# 🧠 Neural Network Model
# =========================================================
model = Pipeline([
    ("scaler", StandardScaler()),
    ("nn", MLPClassifier(
        hidden_layer_sizes=(128, 64, 32), 
        activation="relu",
        solver="adam",
        learning_rate_init=0.001,
        max_iter=500,
        early_stopping=True,
        random_state=42
    ))
])

# 📌 train
model.fit(X_train, y_train)

# 📌 test
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {acc:.4f}")
print("Confusion Matrix:")
print(cm)

# 📌 save model
joblib.dump(model, "models/nn_model.pkl")
joblib.dump(le, "models/label_encoder.pkl")

print("✅ NN model saved!")