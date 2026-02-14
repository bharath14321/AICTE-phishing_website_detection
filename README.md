# AICTE-phishing_website_detection
Phishing Website Detection using Machine Learning (Random Forest) - AICTE Internship Project
# Phishing Website Detection using Machine Learning

This project was developed as part of the AICTE Internship Program.

##  Project Overview

Phishing attacks are one of the most common cybersecurity threats. Fraudulent websites mimic legitimate websites to steal sensitive information such as passwords, credit card details, and personal data.

This project uses Machine Learning to automatically classify websites as:

- Legitimate
- Phishing

The model is built using a Random Forest Classifier and trained on a labeled dataset of 10,000 websites.

---

##  Features

- Data preprocessing and cleaning
- Feature engineering using URL-based attributes
- Random Forest classification model
- Model evaluation using accuracy, precision, recall, and F1-score
- Confusion matrix visualization
- Feature importance analysis
- Real-time URL prediction
- Model saving using joblib

---

##  Machine Learning Model

- Algorithm: Random Forest Classifier
- Dataset Size: 10,000 labeled websites
- Train-Test Split: 80% training / 20% testing
- Model Parameters:
  - n_estimators = 300
  - max_depth = 20

###  Model Performance

- Accuracy: 86%
- Precision (Phishing): 0.95
- Recall (Phishing): 0.76
- F1-Score: 0.84

---

##  Features Used

The model uses 16 numerical features including:

- URL Length
- URL Depth
- Presence of IP address
- HTTPS usage
- Redirection
- DNS record
- Domain age
- iFrame usage
- Mouse-over behavior
- And more
 Known Limitation

The real-time URL prediction feature uses simplified feature extraction based on URL structure.

Some advanced features from the training dataset (such as DNS record, domain age, web traffic, and browser behavior indicators) are not computed in real time.

Because of this, certain legitimate websites may occasionally be predicted as phishing.

This limitation does not affect the trained model’s performance on the original dataset but highlights the need for advanced real-time feature extraction in future improvements.

---

##  How to Run the Project

###  Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/phishing-website-detection.git
cd phishing-website-detection
