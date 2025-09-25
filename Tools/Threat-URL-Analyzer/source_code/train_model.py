import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from extract_features import extract_url_features

# Load dataset
df = pd.read_csv("url_dataset_1.csv") # Enter the dataset names from the present files

# Label mapping
label_mapping = {
    "benign": 0,
    "phishing": 1,
    "defacement": 2,
    "malware": 3
}

df['type'] = df['type'].map(label_mapping)
df = df.dropna(subset=['type'])

# Show class distribution
print("Class distribution:")
print(df['type'].value_counts())

# Extract features
X = [extract_url_features(url) for url in df['url']]
X = pd.DataFrame(X)
y = df['type'].astype(int)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model with class balancing
model = RandomForestClassifier(class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# Evaluation
print("\nClassification Report:")
print(classification_report(y_test, model.predict(X_test)))

# Save model
joblib.dump(model, "model.pkl")
print("\nModel saved as model.pkl")
