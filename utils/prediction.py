import joblib
import numpy as np

model = joblib.load("models/rf_model.pkl")
position_map = {"D": 0, "F": 1, "GK": 2}
label_map = {0: "High", 1: "Low", 2: "Medium"}

def predict_risk(position, load, per_min, max_hr, min_hr, avg_hr):
    pos_encoded = position_map.get(position, 0)
    X = np.array([[pos_encoded, load, per_min, max_hr, min_hr, avg_hr]])
    pred = model.predict(X)[0]
    return label_map.get(pred, "Unknown")
