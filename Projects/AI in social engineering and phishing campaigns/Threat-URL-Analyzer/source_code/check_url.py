import joblib
import pandas as pd
from extract_features import extract_url_features

# Load saved model
model = joblib.load("model.pkl")

# Numeric label to string name mapping
label_names = {
    0: "Benign",
    1: "Phishing",
    2: "Defacement",
    3: "Malware"
}

def check_url(url):
    features = extract_url_features(url)
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    return label_names.get(prediction[0], "Unknown")

# User input
if __name__ == "__main__":
    url = input("Enter a URL to check: ")
    result = check_url(url)
    print("Result:", result)
