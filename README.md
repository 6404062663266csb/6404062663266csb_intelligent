 🧠 Model 1: BMI Classification (Machine Learning)

📌 Overview

This model is developed to classify a user's body condition based on **Body Mass Index (BMI)**. It predicts categories such as:

* Underweight
* Normal
* Overweight
* Obese

---

 📊 Dataset

* Type: Structured Data (CSV)
* Features:

  * Weight (kg)
  * Height (cm)
  * Age
  * Gender

The dataset is generated based on standard BMI calculation principles.

---

⚙️ Preprocessing

* Convert categorical data (Gender) into numerical values
* Clean and validate input data
* Ensure data is in numeric format for model training

---

 🤖 Model

* Algorithm: Machine Learning Classifier
* Output: BMI category (classification)

---

🎯 Function

The model takes user input and predicts the BMI category, helping users understand their health condition.

---

## 🧠 Model 2: Student Pass/Fail Prediction (Neural Network)

 📌 Overview

This model predicts whether a student will **Pass or Fail** using a Neural Network based on study behavior and performance.

---

📊 Dataset

* Type: Structured Data (CSV)

* Features:

  * Hours_Studied
  * Sleep_Hours
  * Attendance
  * Previous_Grade
  * Internet_Usage

* Target:

  * Pass / Fail

---

 ⚙️ Preprocessing

* Encode target labels (Pass = 1, Fail = 0)
* Normalize/scale input features (if applied)
* Split data into training and testing sets

---

 🤖 Model

* Algorithm: Neural Network (MLPClassifier)
* Hidden Layers: (64, 32)
* Activation Function: ReLU

---

 🎯 Function

The model predicts student performance based on behavioral and academic factors, helping identify potential academic outcomes.

---

🔍 Comparison of Models

| Feature | Model 1 (BMI)         | Model 2 (NN Student) |
| ------- | --------------------- | -------------------- |
| Type    | Machine Learning      | Neural Network       |
| Purpose | Health classification | Academic prediction  |
| Input   | Physical data         | Study behavior       |
| Output  | BMI category          | Pass / Fail          |

---

 📌 Conclusion

Both models demonstrate how Machine Learning and Neural Networks can be applied to solve real-world problems:

* Model 1 focuses on health classification
* Model 2 focuses on academic performance prediction

This project highlights the practical use of AI in different domains.
