from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

sentences=[
    "python programming language",
    "machine Learning models",
    "data science analysis",
    "football match today",
    "cricket players practice"
]
vec=TfidfVectorizer()
k=KMeans(n_clusters=2)
cluster =k.fit_predict(vec.fit_transform(sentences))
print("Cluster Results:\n")

for i in range(len(sentences)):
  s=sentences[i]
  c=cluster[i]
  print("Sentence:", s)
  print("Cluster:", c)
  print()
