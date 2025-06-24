# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.pipeline import Pipeline
import joblib

# Load datasets
true_df = pd.read_csv('dataset/True.csv')
fake_df = pd.read_csv('dataset/Fake.csv')

true_df['label'] = 'REAL'
fake_df['label'] = 'FAKE'

df = pd.concat([true_df, fake_df])
X = df['text']
y = df['label']

# Create a pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', PassiveAggressiveClassifier(max_iter=50))
])

# Train-test split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
pipeline.fit(X_train, y_train)

# Save model
joblib.dump(pipeline, 'model/fake_news_model.pkl')
print("Model saved to 'model/fake_news_model.pkl'")
