import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#dataset
#4 data sets are fine if you took 4 here bottom also you need to take 4 not 6
text_data=[
    "free ticket win",
    "good morning",
    "earn money online",
    "how are you",
    "claim your prize",
    "nice to meet you!"
]
labels=[1,0,1,0,1,0]

data=pd.DataFrame({"msg":text_data,"target":labels})
print("DatasetvUsed:")
print(data)

#convert text into numbers
vector=CountVectorizer()
X=vector.fit_transform(data["msg"])
y=data["target"]

#train model
lr=LogisticRegression()
lr.fit(X,y)

#Prediction
test=["win free ticket"]
text_vec=vector.transform(test)
prediction=lr.predict(text_vec)
print("\nTesting Message:",test[0])

if prediction[0]==1:
  print("Prediction: Spam Message")
else:
  print("Prediction: Normal Message")
