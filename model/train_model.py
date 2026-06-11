import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

print("Treinando IA avançada...")

fake = pd.read_csv("data/fake.csv")
true = pd.read_csv("data/true.csv")

fake["label"] = 0
true["label"] = 1

data = pd.concat([fake, true])

# 🔥 garantir texto válido
data = data.dropna()
data["text"] = data["text"].astype(str)

X = data["text"]
y = data["label"]

vectorizer = TfidfVectorizer(
    max_features=10000,
    stop_words="english"
)

X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=500)

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print(f"Precisão real: {accuracy * 100:.2f}%")

joblib.dump(model, "model/fake_news_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Modelo salvo com sucesso!")