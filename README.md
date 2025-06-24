# 🧠 Fake News Detection Using Machine Learning
*A project by Vishv Gehlot, AI/ML Intern at BrainWave Matrix Solution*

---

## 📘 Overview

In an age of information overload, distinguishing between **real** and **fake** news is more crucial than ever. This project focuses on building a **Fake News Detection** system using classical machine learning techniques to identify misinformation based on article content.

---

## 🎯 Objectives

- 🧹 Clean and preprocess a real-world dataset of news articles.
- 🤖 Train multiple ML models to classify news as **real** or **fake**.
- 📈 Evaluate models using robust performance metrics.
- 🌐 Provide a web-based interface for live prediction (Flask integration coming soon).

---

## 📊 Dataset

- **Source:** [Kaggle - Fake and Real News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)
- **Features:**
  - `title`: Headline of the article
  - `text`: Full body of the article
  - `label`: 0 = Real, 1 = Fake

---

## 🔧 Preprocessing Steps

- Convert text to lowercase
- Remove punctuation and special characters
- Tokenize text using **NLTK**
- Remove common **stopwords**
- Apply **lemmatization**
- Transform text using **TF-IDF** vectorization

---

## 🤖 Models Used

| Model                  | Accuracy | Precision | Recall | F1-Score |
|-----------------------|----------|-----------|--------|----------|
| Logistic Regression   | 95.2%    | 94.8%     | 95.7%  | 95.2%    |
| Naive Bayes           | 92.3%    | 90.2%     | 93.5%  | 91.8%    |
| Random Forest         | 96.1%    | 95.9%     | 96.3%  | 96.1%    |
| Support Vector Machine| 94.7%    | 94.2%     | 95.1%  | 94.6%    |

✅ All models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 🛠️ Tech Stack

- **Python**
- **scikit-learn**
- **pandas**, **numpy**
- **nltk**
- **matplotlib**, **seaborn**

---

## 🌐 Web Integration (Planned)

- ✅ Flask web app for user input and prediction
- 🔄 Model integration using `joblib`
- 🧪 Simple UI to paste news and get result (Real / Fake)

---

## 🚀 Future Enhancements

- 🧠 Upgrade to transformer models like **BERT** or **LSTM**
- ☁️ Deploy using **Docker**, **AWS**, or **GCP**
- 🔐 Add API-based fake news scanning endpoint

---

## 📄 License

This project is intended for **academic and educational use only**.  
For commercial use or collaboration, please contact the author.

---

## 👤 Author

**Vishv Gehlot**  
AI/ML Intern @ BrainWave Matrix Solution  
📧 Email: `vishvgehlot10.email@example.com`

---

## 🌟 Feedback & Support

If you found this project useful, consider giving it a ⭐️ and sharing it!  
Feel free to fork, open issues, or suggest improvements.

---
