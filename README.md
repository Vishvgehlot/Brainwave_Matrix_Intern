# Brainwave_Matrix_Intern

# 📰 Fake News Detection Using Machine Learning

## 🚀 Project Overview

This project aims to build a **Fake News Detection** system using classical machine learning algorithms. Given the rising issue of misinformation, especially on social media, this model helps classify news articles as **real** or **fake** based on their content.

---

## 📌 Objectives

- Preprocess and clean a dataset containing news articles.
- Build and train machine learning models for binary classification.
- Evaluate model performance using standard metrics.
- Deploy a basic pipeline for detecting fake news.

---

## 📂 Dataset

- **Source:** [Kaggle - Fake and Real News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)
- **Features:**
  - `title`: Headline of the article.
  - `text`: Full content of the article.
  - `label`: 0 = Real, 1 = Fake

---

## 🧹 Preprocessing Steps

- Lowercasing and punctuation removal  
- Tokenization using NLTK  
- Stopword removal  
- Lemmatization/Stemming  
- Vectorization using **TF-IDF** or **CountVectorizer**

---

## 🧠 Models Used

- ✅ Logistic Regression  
- ✅ Multinomial Naive Bayes  
- ✅ Random Forest Classifier  
- ✅ Support Vector Machine (SVM)

---

## 🧪 Evaluation Metrics

Each model was evaluated based on:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

### 📊 Sample Performance:

| Model                | Accuracy | Precision | Recall | F1-Score |
|---------------------|----------|-----------|--------|----------|
| Logistic Regression | 95.2%    | 94.8%     | 95.7%  | 95.2%    |
| Naive Bayes         | 92.3%    | 90.2%     | 93.5%  | 91.8%    |
| Random Forest       | 96.1%    | 95.9%     | 96.3%  | 96.1%    |
| SVM                 | 94.7%    | 94.2%     | 95.1%  | 94.6%    |

---

## 🛠️ Technologies

- Python  
- scikit-learn  
- pandas  
- numpy  
- nltk  
- matplotlib / seaborn (for visualization)

---

## 💡 Future Enhancements

- Integrate with a Flask web app for UI-based detection  
- Try deep learning models like **BERT** or **LSTM**  
- Deploy the model using **Docker** or on **AWS/GCP**

---

## 🧾 License

This project is for academic and educational purposes. Commercial use is not permitted without permission.

---

## 📬 Contact

**Author:** Vishv Gehlot 
**Role:** AI/ML Intern  
**Company:** BrainWave Matrix Solution  
**Email:** vishvgehlot10.email@example.com

---

## ⭐️ Don't forget to star this repo if you find it helpful!

