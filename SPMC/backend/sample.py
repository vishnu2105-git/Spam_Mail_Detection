import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Assuming you have a fitted TF-IDF vectorizer
vectorizer = TfidfVectorizer()
# Fit your vectorizer on training data here
joblib.dump(vectorizer, 'app/vectorizer.joblib')

