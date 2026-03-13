# Program: Find weight of a specific term in documents using TF-IDF

from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "data science is fun",
    "python is used in data science",
    "machine learning and data science"
]

# Term to check weight
term = "data"

# Create TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform documents
tfidf_matrix = vectorizer.fit_transform(documents)

# Get feature names
feature_names = vectorizer.get_feature_names_out()

# Find index of the specific term
term_index = list(feature_names).index(term)

print("TF-IDF Weights for term:", term)

# Print TF-IDF weight in each document
for i, doc in enumerate(documents):
    weight = tfidf_matrix[i, term_index]
    print(f"Document {i+1}: {weight}")
