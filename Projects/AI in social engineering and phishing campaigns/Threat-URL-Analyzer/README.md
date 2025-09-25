# 🔐 URL Threat Classification Tool

A python-based cybersecurity tool that detects and classifies malicious URLs into "Phishing", "Defacement", "Malware", or "Benign" categories based on extracted structural features.

---

## 📌 Problem Statement

With the rise in cyberattacks through malicious URLs, there is a growing need for an automated solution to detect harmful links before they cause damage. This tool addresses that gap by using ML to classify URLs based on patterns and indicators of malicious intent.

---

## 🎯 Objective

To develop a practical, lightweight, and efficient tool that can:
- Analyze URLs using engineered features
- Classify them into one of four threat categories
- Help users preemptively block harmful web links

---

## ⚙️ Setup Instructions

### 🔧 Prerequisites
- Python 3.9+ (3.9.7 as it is used while making the tool)
- pip

### 📦 Install Dependencies
```cmd
pip install -r requirements.txt
```

### 🚀 Run the Tool
```cmd
python train_model.py
```
This generates a report of the provided csv file.
(The csv file should contain only 2 columns,
one containing the url,
the other containing its type out of the given).
```

```cmd
python check_url.py
```
Then input a URL when prompted.
(This tells if the input url is 'Phishing', 'Malware', 'Defacement' or 'Benign'.)
---

## 🧠 Features Extracted
- URL length, number of subdomains
- Presence of IP address, `@`, `-`, etc.
- Use of HTTPS
- Query parameters and encoded characters
- Suspicious keywords like `login`, `verify`, `password`, etc.

---

## 🛠 Code Structure

```
tool/
├── source_code/
│   ├── check_url.py            # Main script for user input & prediction
│   ├── train_model.py          # Model training & evaluation
│   └── extract_features.py     # Feature extraction from URLs
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 📊 Model Details

- **Algorithm:** Random Forest Classifier  
- **Training Data:** Custom URL dataset (`url_dataset_.csv`)
    (Source: Kaggle)
- **Classes:** Benign (0), Phishing (1), Defacement (2), Malware (3)  
- **Class Balancing:** Enabled with `class_weight='balanced'`

---

## 📈 Sample Output

```
Enter a URL to check: http://free-login.verify-acc.com/login
Result: Phishing
```

---

## ⚖️ License

MIT License. See `LICENSE` for more information.

---

## 📌 Disclaimer

This tool is for educational and research purposes only. It should not be used in real-world security systems without further testing and validation.
