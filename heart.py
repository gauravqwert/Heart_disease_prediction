# import pandas as pd
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.pipeline import Pipeline
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
#
# # ─────────────────────────────────────────────────────────────
# # 1. Load and Preprocess Data
# # ─────────────────────────────────────────────────────────────
# df = pd.read_csv("data.csv")
# print(df.head())
#
# # BMI calculation (if not in dataset)
# df["BMI"] = df["Weight_kg"] / ((df["Height_cm"] / 100) ** 2)
#
# # Label generation functions
# def heart_attack_risk(row):
#     score = 0
#     if row["Age"] >= 60: score += 1
#     if row["BMI"] >= 30: score += 1
#     if str(row["Smoker"]).lower() == "yes": score += 1
#     if str(row["Exercise_Freq"]).lower() in ["never", "sometimes"]: score += 1
#     if str(row["Diet_Quality"]).lower() in ["poor", "average"]: score += 1
#     if str(row["Alcohol_Consumption"]).lower() in ["low","high", "moderate"]: score += 1
#     if row["Sleep_Hours"] < 6: score += 1
#     if row["Cholesterol"] >= 240: score += 1
#     if row["Blood_Pressure"] >= 140: score += 1
#     if str(row["heredity"]).lower() == "yes": score += 1
#     if str(row["Chronic_Disease"]).lower() == "yes": score += 1
#     if str(row["hypertension"]).lower() == "yes": score += 1
#     return int(score >= 6)
#
# def heart_failure_risk(row):
#     score = 0
#     if row["Age"] >= 65: score += 1
#     if row["BMI"] >= 30: score += 1
#     if str(row["Smoker"]).lower() == "yes": score += 1
#     if str(row["Alcohol_Consumption"]).lower() in ["moderate", "high"]: score += 1
#     if row["Cholesterol"] >= 240: score += 1
#     if row["Blood_Pressure"] >= 140: score += 1
#     if str(row["heredity"]).lower() == "yes": score += 1
#     if str(row["Chronic_Disease"]).lower() == "yes": score += 1
#     if str(row["hypertension"]).lower() == "yes": score += 1
#     if str(row["Exercise_Freq"]).lower() == "never": score += 1
#     return int(score >= 5)
#
# def bypass_surgery_need(row):
#     score = 0
#     if row["Age"] >= 65: score += 1
#     if row["BMI"] >= 32: score += 1
#     if row["Cholesterol"] >= 280: score += 1
#     if row["Blood_Pressure"] >= 160: score += 1
#     if str(row["Heredity"]).lower() == "yes": score += 1
#     if str(row["Chronic_Disease"]).lower() == "yes": score += 1
#     if str(row["hypertension"]).lower() == "yes": score += 1
#     if str(row["Exercise_Freq"]).lower() == "never": score += 1
#     return int(score >= 5)
#
# def stroke_risk(row):
#     score = 0
#     if row["Age"] >= 60: score += 1
#     if str(row["hypertension"]).lower() == "yes": score += 1
#     if row["Cholesterol"] >= 240: score += 1
#     if row["Blood_Pressure"] >= 140: score += 1
#     if str(row["Chronic_Disease"]).lower() == "yes": score += 1
#     if str(row["Smoker"]).lower() == "yes": score += 1
#     if row["Sleep_Hours"] < 6: score += 1
#     if row["BMI"] >= 30: score += 1
#     if str(row["Exercise_Freq"]).lower() == "never": score += 1
#     if str(row["Heredity"]).lower() == "yes": score += 1
#     return int(score >= 5)
#
# # Add target labels
# df["Heart_Attack_Risk"] = df.apply(heart_attack_risk, axis=1)
# df["Heart_Failure_Risk"] = df.apply(heart_failure_risk, axis=1)
# df["Bypass_Required"] = df.apply(bypass_surgery_need, axis=1)
# df["Stroke_Risk"] = df.apply(stroke_risk, axis=1)
#
# # ─────────────────────────────────────────────────────────────
# # 2. Set up features and pipeline
# # ─────────────────────────────────────────────────────────────
# FEATURES = [
#     "Age", "Gender", "Height_cm", "Weight_kg", "BMI",
#     "Smoker", "Exercise_Freq", "Diet_Quality", "Alcohol_Consumption",
#     "Sleep_Hours", "Cholesterol", "Blood_Pressure",
#     "Ethnicity", "herdity", "Chronic_Disease", "hypertension"
# ]
#
# NUM_COLS = [
#     "Age", "Height_cm", "Weight_kg", "BMI",
#     "Sleep_Hours", "Cholesterol", "Blood_Pressure"
# ]
#
# CAT_COLS = [
#     "Gender", "Smoker", "Exercise_Freq", "Diet_Quality",
#     "Alcohol_Consumption", "Ethnicity", "herdity",
#     "Chronic_Disease", "hypertension"
# ]
#
# preprocessor = ColumnTransformer([
#     ("num", StandardScaler(), NUM_COLS),
#     ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), CAT_COLS)
# ])
#
# def train_model(target_col):
#     X = df[FEATURES]
#     y = df[target_col]
#     X_train, X_test, y_train, y_test = train_test_split(
#         X, y, test_size=0.2, random_state=42
#     )
#     pipeline = Pipeline([
#         ("prep", preprocessor),
#         ("clf", RandomForestClassifier(n_estimators=300, class_weight="balanced", random_state=42))
#     ])
#     pipeline.fit(X_train, y_train)
#     acc_train = accuracy_score(y_train, pipeline.predict(X_train))
#     acc_test = accuracy_score(y_test, pipeline.predict(X_test))
#     return pipeline, acc_train, acc_test
#
# # ─────────────────────────────────────────────────────────────
# # 3. Train all 4 models
# # ─────────────────────────────────────────────────────────────
# print("🔄 Training models...")
# model_attack, acc_attack_train, acc_attack_test = train_model("Heart_Attack_Risk")
# model_failure, acc_failure_train, acc_failure_test = train_model("Heart_Failure_Risk")
# model_bypass, acc_bypass_train, acc_bypass_test = train_model("Bypass_Required")
# model_stroke, acc_stroke_train, acc_stroke_test = train_model("Stroke_Risk")
# print("✅ Models trained.\n")
#
# # # ─────────────────────────────────────────────────────────────
# # # 4. Input Prompt
# # # ─────────────────────────────────────────────────────────────
# def ask(prompt, cast, allowed=None):
#     while True:
#         raw = input(f"{prompt}: ").strip()
#         try:
#             if cast in (int, float):
#                 return cast(raw)
#             norm = raw.lower()
#             if allowed:
#                 al = [a.lower() for a in allowed]
#                 if norm not in al: raise ValueError
#                 return allowed[al.index(norm)]
#             return raw.title()
#         except:
#             print("  ✖ Invalid input. Please try again.")
#
# GENDER_LST = ["Male", "Female", "Other"]
# SMOKER_LST = ["Yes", "No"]
# EX_FREQ_LST = ["Daily", "Alternate-Day", "Sometimes", "Never"]
# DIET_LST = ["Poor", "Average", "Good", "Excellent"]
# ALCO_LST = ["None", "Low", "Moderate", "High"]
# ETHNIC_LST = ["White", "Black", "Asian", "Hispanic", "Other"]
# YN_LST = ["Yes", "No"]
#
# # print("Enter patient details to predict 4 risks:\n—")
# # h_cm = ask("Height (cm)", float)
# # w_kg = ask("Weight (kg)", float)
# # bmi = round(w_kg / ((h_cm / 100) ** 2), 1)
#
# # patient = {
# #     "Age": ask("Age (years)", int),
# #     "Gender": ask("Gender [Male/Female/Other]", str, GENDER_LST),
# #     "Height_cm": h_cm,
# #     "Weight_kg": w_kg,
# #     "BMI": bmi,
# #     "Smoker": ask("Smoker [Yes/No]", str, SMOKER_LST),
# #     "Exercise_Freq": ask("Exercise Frequency [Daily/Alternate-Day/Sometimes/Never]", str, EX_FREQ_LST),
# #     "Diet_Quality": ask("Diet Quality [Poor/Average/Good/Excellent]", str, DIET_LST),
# #     "Alcohol_Consumption": ask("Alcohol Consumption [None/Low/Moderate/High]", str, ALCO_LST),
# #     "Sleep_Hours": ask("Sleep Hours per night", float),
# #     "Cholesterol": ask("Cholesterol (mg/dL)", float),
# #     "Blood_Pressure": ask("Systolic BP (mmHg)", float),
# #     "Ethnicity": ask("Ethnicity [White/Black/Asian/Hispanic/Other]", str, ETHNIC_LST),
# #     "herdity": ask("Family History of Heart Disease [Yes/No]", str, YN_LST),
# #     "Chronic_Disease": ask("Diagnosed with Chronic Disease? [Yes/No]", str, YN_LST),
# #     "hypertension": ask("Diagnosed with Hypertension? [Yes/No]", str, YN_LST),
# # }
# #
# # X_new = pd.DataFrame([patient])
# #
# # # ─────────────────────────────────────────────────────────────
# # # 5. Predictions and Output
# # # ─────────────────────────────────────────────────────────────
# # attack_prob = model_attack.predict_proba(X_new)[0, 1]
# # failure_prob = model_failure.predict_proba(X_new)[0, 1]
# # bypass_prob = model_bypass.predict_proba(X_new)[0, 1]
# # stroke_prob = model_stroke.predict_proba(X_new)[0, 1]
# #
# # print("\n Prediction Results:")
# # print(f"•  Heart Attack Risk:     {attack_prob*100:.2f}%")
# # print(f"•  Heart Failure Risk:     {failure_prob*100:.2f}%")
# # print(f"•  Bypass Surgery Likely:  {bypass_prob*100:.2f}%")
# # print(f"•  Stroke Risk:            {stroke_prob*100:.2f}%")
# #
# # print("\n Model Accuracies:")
# # print(f"  Heart Attack   → Train: {acc_attack_train:.2%} | Test: {acc_attack_test:.2%}")
# # print(f"  Heart Failure  → Train: {acc_failure_train:.2%} | Test: {acc_failure_test:.2%}")
# # print(f"  Bypass Surgery → Train: {acc_bypass_train:.2%} | Test: {acc_bypass_test:.2%}")
# # print(f"  Stroke Risk    → Train: {acc_stroke_train:.2%} | Test: {acc_stroke_test:.2%}")
#
# #
# # # heart.py
# # import joblib           # or pickle, keras, etc.
# # import numpy as np
# #
# # _model = joblib.load("model.joblib")   # adjust as needed
# #
# # FEATURE_ORDER = [
# #     "age", "height", "weight",
# #     "cholesterol", "blood_pressure", "smoking",
# #     "alcohol", "sleep", "diet",
# #     "exercise", "heredity", "hypertension"
# # ]
# #
# # def predict_risks(payload: dict[str, float]) -> dict[str, int]:
# #     """Return percentage risks rounded to whole numbers."""
# #     x = np.array([[payload[feat] for feat in FEATURE_ORDER]])
# #     probs = _model.predict_proba(x)     # tailor to your model
# #     return {
# #         "heart_attack":  int(probs[0, 0] * 100),
# #         "heart_failure": int(probs[0, 1] * 100),
# #         "bypass":        int(probs[0, 2] * 100),
# #         "stroke":        int(probs[0, 3] * 100),
# #     }



# heart.py
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# ─────────────────────────────────────────────────────────────
# 1. Load and preprocess data
# ─────────────────────────────────────────────────────────────
df = pd.read_csv("data.csv")
df.rename(columns=str.strip, inplace=True)
df.rename(columns={"herdity": "heredity"}, inplace=True)

df["BMI"] = df["Weight_kg"] / ((df["Height_cm"] / 100) ** 2)

def heart_attack_risk(row):
    score = 0
    if row["Age"] >= 60: score += 1
    if row["BMI"] >= 30: score += 1
    if str(row["Smoker"]).lower() == "yes": score += 1
    if str(row["Exercise_Freq"]).lower() in ["never", "sometimes"]: score += 1
    if str(row["Diet_Quality"]).lower() in ["poor", "average"]: score += 1
    if str(row["Alcohol_Consumption"]).lower() in ["low", "moderate", "high"]: score += 1
    if row["Sleep_Hours"] < 6: score += 1
    if row["Cholesterol"] >= 240: score += 1
    if row["Blood_Pressure"] >= 140: score += 1
    if str(row["heredity"]).lower() == "yes": score += 1
    if str(row["Chronic_Disease"]).lower() == "yes": score += 1
    if str(row["hypertension"]).lower() == "yes": score += 1
    return int(score >= 6)

def heart_failure_risk(row):
    score = 0
    if row["Age"] >= 65: score += 1
    if row["BMI"] >= 30: score += 1
    if str(row["Smoker"]).lower() == "yes": score += 1
    if str(row["Alcohol_Consumption"]).lower() in ["moderate", "high"]: score += 1
    if row["Cholesterol"] >= 240: score += 1
    if row["Blood_Pressure"] >= 140: score += 1
    if str(row["heredity"]).lower() == "yes": score += 1
    if str(row["Chronic_Disease"]).lower() == "yes": score += 1
    if str(row["hypertension"]).lower() == "yes": score += 1
    if str(row["Exercise_Freq"]).lower() == "never": score += 1
    return int(score >= 5)

def bypass_surgery_need(row):
    score = 0
    if row["Age"] >= 65: score += 1
    if row["BMI"] >= 32: score += 1
    if row["Cholesterol"] >= 280: score += 1
    if row["Blood_Pressure"] >= 160: score += 1
    if str(row["heredity"]).lower() == "yes": score += 1
    if str(row["Chronic_Disease"]).lower() == "yes": score += 1
    if str(row["hypertension"]).lower() == "yes": score += 1
    if str(row["Exercise_Freq"]).lower() == "never": score += 1
    return int(score >= 5)

def stroke_risk(row):
    score = 0
    if row["Age"] >= 60: score += 1
    if str(row["hypertension"]).lower() == "yes": score += 1
    if row["Cholesterol"] >= 240: score += 1
    if row["Blood_Pressure"] >= 140: score += 1
    if str(row["Chronic_Disease"]).lower() == "yes": score += 1
    if str(row["Smoker"]).lower() == "yes": score += 1
    if row["Sleep_Hours"] < 6: score += 1
    if row["BMI"] >= 30: score += 1
    if str(row["Exercise_Freq"]).lower() == "never": score += 1
    if str(row["heredity"]).lower() == "yes": score += 1
    return int(score >= 5)

df["Heart_Attack_Risk"] = df.apply(heart_attack_risk, axis=1)
df["Heart_Failure_Risk"] = df.apply(heart_failure_risk, axis=1)
df["Bypass_Required"] = df.apply(bypass_surgery_need, axis=1)
df["Stroke_Risk"] = df.apply(stroke_risk, axis=1)

# ─────────────────────────────────────────────────────────────
# 2. Features & Preprocessing
# ─────────────────────────────────────────────────────────────
FEATURES = [
    "Age", "Gender", "Height_cm", "Weight_kg", "BMI",
    "Smoker", "Exercise_Freq", "Diet_Quality", "Alcohol_Consumption",
    "Sleep_Hours", "Cholesterol", "Blood_Pressure",
    "Ethnicity", "heredity", "Chronic_Disease", "hypertension"
]

NUM_COLS = [
    "Age", "Height_cm", "Weight_kg", "BMI",
    "Sleep_Hours", "Cholesterol", "Blood_Pressure"
]

CAT_COLS = [
    "Gender", "Smoker", "Exercise_Freq", "Diet_Quality",
    "Alcohol_Consumption", "Ethnicity", "heredity",
    "Chronic_Disease", "hypertension"
]

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), NUM_COLS),
    ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), CAT_COLS)
])

# ─────────────────────────────────────────────────────────────
# 3. Model Training Pipeline
# ─────────────────────────────────────────────────────────────
def train_and_save_model(target_col, filename):
    X = df[FEATURES]
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline = Pipeline([
        ("prep", preprocessor),
        ("clf", RandomForestClassifier(n_estimators=300, random_state=42))
    ])

    pipeline.fit(X_train, y_train)

    joblib.dump(pipeline, filename)

    train_acc = accuracy_score(y_train, pipeline.predict(X_train))
    test_acc = accuracy_score(y_test, pipeline.predict(X_test))
    print(f"{target_col} → Train: {train_acc:.2%} | Test: {test_acc:.2%}")

# ─────────────────────────────────────────────────────────────
# 4. Save full pipeline
# ─────────────────────────────────────────────────────────────
print("🔄 Training models...\n")

train_and_save_model("Heart_Attack_Risk", "model_heart_attack.joblib")
train_and_save_model("Heart_Failure_Risk", "model_heart_failure.joblib")
train_and_save_model("Bypass_Required", "model_bypass.joblib")
train_and_save_model("Stroke_Risk", "model_stroke.joblib")

print("\n✅ All models trained and saved.")