# ----------------------------------------
# Phishing Website Detection Project
# ----------------------------------------

import pandas as pd
import numpy as np
import re
from urllib.parse import urlparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


# ----------------------------------------
# Step 1: Load Dataset
# ----------------------------------------
def load_data():
    url = "https://raw.githubusercontent.com/shreyagopal/Phishing-Website-Detection-by-Machine-Learning-Techniques/master/DataFiles/data.csv"
    data = pd.read_csv(url)
    return data


# ----------------------------------------
# Step 2: Preprocess Data
# ----------------------------------------
def preprocess_data(data):
    X = data.drop(["Label", "Domain"], axis=1)
    y = data["Label"]
    return X, y


# ----------------------------------------
# Step 3: Train Model
# ----------------------------------------
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=20,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    return model


# ----------------------------------------
# Step 4: Feature Extraction for Real URL
# ----------------------------------------
def extract_features(url):
    features = []

    # 1. Have_IP
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    features.append(1 if re.search(ip_pattern, url) else 0)

    # 2. Have_At
    features.append(1 if "@" in url else 0)

    # 3. URL_Length
    features.append(1 if len(url) > 54 else 0)

    # 4. URL_Depth
    path = urlparse(url).path
    depth = path.count('/')
    features.append(depth)

    # 5. Redirection
    features.append(1 if "//" in url[7:] else 0)

    # 6. https_Domain
    features.append(1 if url.startswith("https") else 0)

    # 7. TinyURL
    shortening_services = ["bit.ly", "tinyurl", "goo.gl"]
    features.append(1 if any(service in url for service in shortening_services) else 0)

    # Fill remaining features with 1 (assumed legitimate defaults)
    while len(features) < 16:
        features.append(1)

    return features


# ----------------------------------------
# Step 5: Main Function
# ----------------------------------------
def main():

    print("Loading dataset...")
    data = load_data()

    print("Preprocessing data...")
    X, y = preprocess_data(data)

    print("Training model...")
    model = train_model(X, y)

    print("Saving model...")
    joblib.dump(model, "phishing_model.pkl")

    print("\nModel saved successfully!")

    # Real-time prediction
    user_url = input("\nEnter a URL to check: ")

    features = extract_features(user_url)

    prediction = model.predict([features])

    if prediction[0] == 1:
        print("This website is predicted as PHISHING")
    else:
        print("This website is predicted as LEGITIMATE")


# ----------------------------------------
# Run Program
# ----------------------------------------
if __name__ == "__main__":
    main()
